# Ch 1 build — row store vs column store

## Instructions

Same dataset, two architectures: run one analytical query workload against a row store (SQLite) and a column store (DuckDB). Measure the gap. Instruments the chapter's operational-vs-analytical divide directly.

Timebox: 3.0h hard stop. Unpolished is correct.

## Context

- A page is a fixed-length block of consecutive data that is loaded from storage.
- Both row and column stores store tabular data.
- Tabular data consists of cells (individual values) that are organized into a two-dimensional grid of rows and columns.
- In a row store, cells that belong to the same row are stored consecutively. Because the data types of the cells in the row are usually not all the same, compression techniques are usually not effective for reducing storage. This prioritizes loading as many full rows as possible whenever a page is loaded, so iterating row by row requires less loads. However, iterating column by column will require multiple loads if the entire dataset does not fit on a single page.
  - Loading a single row requires one page load if the row fits on a page.
  - Loading a single column requires multiple page loads if the dataset does not fit on a page.
- In a column store, cells that belong to the same column are stored consecutively. Because the data type of the column is fixed, compression techniques can be used to store the same amount of data in with less space. This prioritizes loading as many full columns as possible whenever a page is loaded, so iterating through full columns requires less loads. However, iterating row by row will require multiple loads if the entire dataset does not fit on a single page.
  - Loading a single row requires multiple page loads if the dataset does not fit on a page.
  - Loading a single column requires one page load if the column fits on a page.

## Hypothesis

- As the number of column scans in a query increases, the performance improvment from using a column store over a row store will also increase.

## Experiment

### Variables

- Independent variable: Number of column scans in a query
  - Range: 0 to 6 inclusive
- Dependent variable: Performance improvement from using a column store over a row store
  - `% improvement = (time_row_store - time_column_store) / time_column_store * 100%`
- Controlled variables
  - Dataset: "2026 Data, Q1" from [Backblaze Drive Stats data set](https://www.backblaze.com/cloud-storage/resources/hard-drive-test-data)
    - Relevant columns:
      - 0: date (date)
      - 1: serial_number (string)
        - run a query to find the maximum length, or go with 2^8
      - 2: model (string)
      - 3: capacity_bytes (unsigned integer)
        - Go with 2^64 as the largest value
      - 4: failure (0 or 1)
        - Use boolean
      - 11+: smart_x_normalized and smart_x_raw (unsigned integers)
        - raw has a max of about 2^64, while normalized is 2^8
  - System: The same computer will be used for all tests (Macbook M2 Pro).
  - Row store: Sqlite
  - Column store: DuckDB
  - Programming language: Python
  - The type of query: Avg over all values in a column

### Procedure

- A python script will perform the experiment using the following queries

#### Queries

- The queries will average over the following values
  - capacity_bytes
  - smart_5_raw (reallocated sector count)
  - smart_187_raw (reported uncorrectable errors)
  - smart_188_raw (command timeout)
  - smart_197_raw (current pending sector count)
  - smart_198_raw (offline uncorrectable count)

### Results

#### Loading stores

- Loading both stores with data from the CSV files took almost 10 hours. Iterating through each file, line by line, and inserting rows into both stores in batches of 100 rows was very slow. Maybe it is because of python being a slow language, but probably also due to the small batch size.
- The row store had a size of over 20 G, while the column store had a size of over 2 GB.

#### Column scan queries

| Column scans | Row store (s) | Column store (s) | % speed up (column vs row) |
| ------------ | ------------- | ---------------- | -------------------------- |
| 0            | 0.001         | 0.014            | -92.9%                     |
| 1            | 14.571        | 0.040            | 36,327.5%                  |
| 2            | 16.740        | 0.063            | 26,471.4%                  |
| 3            | 46.167        | 0.050            | 92,234.0%                  |
| 4            | 47.622        | 0.051            | 93,276.5%                  |
| 5            | 50.278        | 0.051            | 98,484.3%                  |
| 6            | 50.433        | 0.056            | 89,958.9%                  |

## Analysis

- The column store was a tenth of the size of the row store at just 2 GB. This was achieved due to data compression
- At 0 column scans, the row store was almost 100% faster than the column store, with near ms latency compared to the column store's over 14 ms latency.
- At 1 column scan, the column store immediately performs significantly better than the row store, with a speed up of over 36,000%. The row store has over 14 seconds of latency while the column store is at 40 ms.
- As the number of column scans increased, the column store maintained a latency between 50 to 63 ms, while the row store latency kept increasing. The row store latency increased by a few seconds or less with each new column scan, except for the jump from 2 to 3 column scans when it jumped 30 seconds. The speed up from using a column store was between 90,000% and 98,000% for 3 to 6 column scans, which was after the large jump in latency for the row store.
- Some factors that might have affected the latency of the row store might be how closely some of the fields in a row are stored closer together. The query with 2 column scans aggregated over the capacity_bytes and smart_raw_5 fields, which appear a lot earlier in the row compared to the smart_raw_187 field. Also, the fields used for the remaining queries were a lot closer to the smart_raw_187 field in the row. So as the row store query engine was iterating throw all the rows, it might have calculated the average of several columns that were close together at the same time. Not sure if this is true.

## Conclusion

- For analytical queries, column stores are much more performant than row stores due to how they store data. Storing columns together allowed for better data compression and faster scanning of values in a column, which are ideal for analytical systems that need to store lots of data efficiently and perform read-only queries on large amounts of that data.
- For point queries, column stores are disadvantageous compared to row stores. Some reasons for this include the storage layout requiring more steps to retrieve a single value from a column. The engine also has extra overhead that helps for analytical queries but slows down a point query. The row store's layout using B-trees requires less steps to read the value from a single row.

## Where I got stuck

- Originally I was filtering on failures, but the number of failures was pretty small, which made aggregating on columns fast. I wanted to iterate over entire columns, so I removed this filter
- Instead of adding group by clauses to add column scans, I stuck with adding average aggregations for each column to be consistent with how the queries are changing.
