import csv
import sqlite3
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from time import perf_counter
from typing import Iterable, Union

import duckdb

DATASET_DIR = "data_Q1_2026/"
ROW_STORE_PATH = "row_store.db"
COLUMN_STORE_PATH = "column_store.duckdb"


@dataclass(frozen=True)
class Query:
    name: str
    sql: str


def format_str(s: str) -> str:
    if not s:
        return "NULL"

    return f"'{s}'"


def format_int(s: str) -> str:
    if not s:
        return "NULL"

    return s


def format_bool(s: str) -> str:
    if not s:
        return "NULL"
    elif s == "1" or s.lower() == "true":
        return "TRUE"
    else:
        return "FALSE"


@dataclass(frozen=True)
class Store:
    name: str
    connection: Union[sqlite3.Connection, duckdb.DuckDBPyConnection]
    cursor: Union[sqlite3.Cursor, duckdb.DuckDBPyConnection]


@dataclass(frozen=True)
class MultiStore:
    stores: Iterable[Store]

    def execute(self, query: Query):
        for store in self.stores:
            print(f"Executing query '{query.name}' for {store.name}")
            store.cursor.execute(query.sql)
            store.connection.commit()
            print(f"Executed query '{query.name}' for {store.name}")

    def close(self):
        for store in self.stores:
            store.connection.close()


def make_drop_table_query() -> Query:
    sql = """
DROP TABLE IF EXISTS drive_stats;
"""
    return Query("drop_table", sql)


def make_create_table_query() -> Query:
    sql = f"""
CREATE TABLE drive_stats (
    date DATE NOT NULL,
    serial_number VARCHAR NOT NULL,
    model VARCHAR NOT NULL,
    capacity_bytes UINT64 NOT NULL,
    failure Boolean NOT NULL,
    datacenter VARCHAR NOT NULL,
    cluster_id UINT8 NOT NULL,
    vault_id UINT16 NOT NULL,
    pod_id UINT8 NOT NULL,
    pod_slot_num UINT8,
    is_legacy_format BOOLEAN NOT NULL,
    {
        ", ".join(
            f"smart_{i}_normalized UINT8, smart_{i}_raw UINT64" for i in range(1, 256)
        )
    }
);
"""
    return Query("create_table", sql)


def format_row(row: list[str]) -> str:
    date = format_str(row[0])
    serial_number = format_str(row[1])
    model = format_str(row[2])
    capacity_bytes = format_int(row[3])
    failure = format_bool(row[4])
    datacenter = format_str(row[5])
    cluster_id = format_int(row[6])
    vault_id = format_int(row[7])
    pod_id = format_int(row[8])
    pod_slot_num = format_int(row[9])
    is_legacy_format = format_bool(row[10])

    smart_values = [""] * 255 * 2
    smart_values[: len(row) - 11] = row[11:]

    sql = f"""
(
    {date},
    {serial_number},
    {model},
    {capacity_bytes},
    {failure},
    {datacenter},
    {cluster_id},
    {vault_id},
    {pod_id},
    {pod_slot_num},
    {is_legacy_format},
    {", ".join(format_int(value) for value in smart_values)}
)
"""
    return sql


def make_insert_query(rows: list[list[str]]) -> Query:
    sql = f"""
INSERT INTO drive_stats
VALUES
{",".join(format_row(row) for row in rows)}
;
"""
    return Query("insert_into", sql)


ZERO_COLUMN_SCAN_QUERY = """
SELECT capacity_bytes
FROM drive_stats
LIMIT 1;
"""

ONE_COLUMN_SCAN_QUERY = """
SELECT AVG(capacity_bytes) AS avg_capacity_bytes
FROM drive_stats;
"""

TWO_COLUMN_SCAN_QUERY = """
SELECT
    AVG(capacity_bytes) AS avg_capacity_bytes,
    AVG(smart_5_raw) AS avg_reallocated_sector_count
FROM drive_stats;
"""

THREE_COLUMN_SCAN_QUERY = """
SELECT
    AVG(capacity_bytes) AS avg_capacity_bytes,
    AVG(smart_5_raw) AS avg_reallocated_sector_count,
    AVG(smart_187_raw) AS avg_reported_uncorrectable_errors
FROM drive_stats;
"""

FOUR_COLUMN_SCAN_QUERY = """
SELECT
    AVG(capacity_bytes) AS avg_capacity_bytes,
    AVG(smart_5_raw) AS avg_reallocated_sector_count,
    AVG(smart_187_raw) AS avg_reported_uncorrectable_errors,
    AVG(smart_188_raw) AS avg_command_timeout
FROM drive_stats;
"""

FIVE_COLUMN_SCAN_QUERY = """
SELECT
    AVG(capacity_bytes) AS avg_capacity_bytes,
    AVG(smart_5_raw) AS avg_reallocated_sector_count,
    AVG(smart_187_raw) AS avg_reported_uncorrectable_errors,
    AVG(smart_188_raw) AS avg_command_timeout,
    AVG(smart_197_raw) AS avg_current_pending_sector_count
FROM drive_stats;
"""

SIX_COLUMN_SCAN_QUERY = """
SELECT
    AVG(capacity_bytes) AS avg_capacity_bytes,
    AVG(smart_5_raw) AS avg_reallocated_sector_count,
    AVG(smart_187_raw) AS avg_reported_uncorrectable_errors,
    AVG(smart_188_raw) AS avg_command_timeout,
    AVG(smart_197_raw) AS avg_current_pending_sector_count,
    AVG(smart_198_raw) AS avg_offline_uncorrectable_errors
FROM drive_stats;
"""

COLUMN_SCAN_QUERIES = [
    ZERO_COLUMN_SCAN_QUERY,
    ONE_COLUMN_SCAN_QUERY,
    TWO_COLUMN_SCAN_QUERY,
    THREE_COLUMN_SCAN_QUERY,
    FOUR_COLUMN_SCAN_QUERY,
    FIVE_COLUMN_SCAN_QUERY,
    SIX_COLUMN_SCAN_QUERY,
]


def create_stores(multi_store: MultiStore):
    multi_store.execute(make_drop_table_query())
    multi_store.execute(make_create_table_query())


def load_stores(path: str, multi_store: MultiStore):
    dir_path = Path(path)
    if not dir_path.exists():
        print(f"Path '{dir_path.name}' does not exist.")

    if not dir_path.is_dir():
        print(f"Path '{dir_path.name}' is not a directory.")

    for csv_file_path in sorted(dir_path.iterdir()):
        with open(csv_file_path) as csv_file:
            reader = csv.reader(csv_file)

            # Skip header row
            next(reader)

            batch = []
            for row in reader:
                if len(batch) == 100:
                    print(f"CSV: {csv_file_path}")
                    multi_store.execute(make_insert_query(batch))

                    batch = []

                batch.append(row)

            if batch:
                print(f"CSV: {csv_file_path}")
                multi_store.execute(make_insert_query(batch))


def run_queries(stores: list[Store]):
    results = [{store.name: 0.0 for store in stores} for _ in COLUMN_SCAN_QUERIES]

    for column_scans, sql in enumerate(COLUMN_SCAN_QUERIES):
        for store in stores:
            print(f"Running query with {column_scans} column scans for {store.name}...")

            start_s = perf_counter()
            store.cursor.execute(sql)
            end_s = perf_counter()
            duration_s = end_s - start_s

            results[column_scans][store.name] = duration_s

            print(
                f"Ran query with {column_scans} column scans for {store.name} in {duration_s} seconds!"
            )
    print()

    print("Results")
    for column_scans, durations_s in enumerate(results):
        print("-" * 20)

        print(f"Column scans: {column_scans}")

        for store_name, duration_s in durations_s.items():
            print(f"Store: {store_name}, Duration: {duration_s:.4f} s")
    print()


def main():
    start_time = datetime.now()

    if len(sys.argv) < 2:
        print("Command is missing")
        exit(1)

    sqlite_con = sqlite3.connect(ROW_STORE_PATH)
    sqlite_cur = sqlite_con.cursor()
    row_store = Store("row_store", sqlite_con, sqlite_cur)

    duckdb_con = duckdb.connect(COLUMN_STORE_PATH)
    duckdb_cur = duckdb_con.cursor()
    column_store = Store("column_store", duckdb_con, duckdb_cur)

    stores = [row_store, column_store]

    multi_store = MultiStore(stores)

    command = sys.argv[1]
    match command:
        case "create-stores":
            create_stores(multi_store)
        case "load-stores":
            load_stores(DATASET_DIR, multi_store)
        case "run-queries":
            run_queries(stores)
        case _:
            print(
                f"Command '{command}' not found. Valid commands include 'create-stores', 'load-stores', 'run-queries'"
            )

    multi_store.close()

    end_time = datetime.now()
    print("Start time:", start_time)
    print("End time:", end_time)

    exit(1)


if __name__ == "__main__":
    main()
