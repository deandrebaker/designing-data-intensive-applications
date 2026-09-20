# Ch 1 — Trade-Offs in Data Systems Architecture

## Distillation (closed-book)

<!-- Book shut. 45 minutes. Full sentences, not fragments — a fragment can't be
     wrong, which is how closed-book recall gets faked without you noticing.
     Mark every claim [sure] or [shaky]. -->

### The question this chapter answers

<!-- One sentence. If you can't write it, you didn't get the chapter. -->

[sure] What are the trade-offs to consider when designing a data system?

- [sure] Data system: A system used for data management.
- [shaky] Data management: The process of accessing and modifying information according to a set of rules.
- [sure] System: A collection of interconnected parts that work together to perform a task.

### Mechanisms

<!-- For each: what it does / how it works / what it costs.
     The cost slot is mandatory. An empty one means you absorbed marketing,
     not engineering — and it's exactly what the explainer rubric scores in
     dimension 2.

     Thin for this chapter. That's correct for ch 1, not a bad recall. -->

#### OLTP (Online Transactional Processing)

- What it does: Performs a sequence of data management operations that either all succeed together or all fail together. When a failure occurs, the system is reverted back to its initial state.

#### OLAP (Online Analytical Processing)

- What it does: Performs analytical queries on data to calculate aggregate statistics.

#### HTAP (Hybrid Transactional Analytical Processing)

- What it does: Performs both OLTP and OLAP operations on the same data.
- How it does it: Uses a single database internally, so no need to transfer data between separate systems.
- What it costs: Does not perform OLTP or OLAP operations as optimally as separate OLTP and OLAP systems since both systems may have different use cases.

#### ETL (Extract-Transform-Load) pipelining

- What it does: Moves data from data sources into a data warehouse for analytical processing. The data must be transformed to match the structure of the data warehouse.
- How it does it: It extracts data from the data sources, perform transformations on the data, then loads the data into the data warehouse.

#### Data pipelining

- What it does: Moves data from a data source into a data lake. The data can be unprocessed.
- How it does it: It extracts data from the data sources, then loads the data into the data lake.

### Trade-offs

<!-- The load-bearing section for this chapter. -->

| Axis               | One side         | Other side          | What decides                                         |
| ------------------ | ---------------- | ------------------- | ---------------------------------------------------- |
| Data processing    | Operational      | Analytical          | Data access patterns                                 |
| Data flow          | System of record | Derived data system | Data consistency requirements                        |
| Hosting            | Self hosting     | Cloud hosting       | Workload predictability                              |
| Cloud architecture | Cloud enabled    | Cloud native        | Infrastructure control                               |
| Node distribution  | Single-node      | Distributed         | Nature of the problem, load, geographic requirements |
| Distributed system | Microservices    | Serverless          | Organization size, workload                          |
| Compute            | Cloud computing  | Super computing     | System function                                      |

### When this breaks

<!-- Failure modes, and the conditions that trigger them. -->

#### Self hosting

- When the workload exceeds beyond the peak capacity, the system cannot serve every request.

#### Cloud hosting

- When a cloud service is down, the system goes down with it until the cloud service recovers.

#### Cloud enabled

- When part of the system fails, unless there's built-in recovery, the system will fail.

#### Single-node systems

- When the machine fails, the entire system fails.
- When the workload exceeds what a single machine can handle, then the system can't process every request well.

#### Distributed systems

- If the communication network between nodes is broken, then it might cause the system to fail.

#### Supercomputing

- When a node fails, the whole system is stopped while the node is repaired.

### Connections

<!-- What this changes about earlier chapters and about your own build.
     Empty for ch 1 — correct. Starts earning its place around ch 6. -->

### Open questions

<!-- WRITE THESE BEFORE OPENING THE BOOK.
     Things you're unsure of. Highest-value section in the file. -->

- What mechanisms were mentioned in this chapter?
- What are the remaining failure modes?
- What an ETL system does?
- How transactional processing work?
- What does transactional processing cost?
- How analytical processing work?
- What does analytical processing cost?
- What does ETL pipelining cost?
- What does data pipelining cost?
- What are the failure modes of operational systems?
- What are the failure modes of analytical systems?
- What are the failure modes of distributed systems?
- What are the failure modes of microservices systems?
- What are the failure modes of serverless systems?

## What I got wrong

<!-- Only after the above is done. 45 minutes. Open the book and correct
     yourself here. Each correction cites a section.

     Watch for two kinds:
       - [shaky] that turned out right — you know more than you think
       - [sure] that turned out wrong — the dangerous kind; raw correctness
         hides these completely

     Every miss goes into review/queue.md. -->

- I didn't think of transactional processing as a mechanism
- I didn't think of analytical processing as a mechanism
- I misunderstood how HLTP works. I thought it internally had 2 systems, but in practice it's just 1 database with OLTP and OLAP operations.
- I didn't think of listing system-of-record and derived data systems in the trade-offs table.
- I forgot about microservices and serverless.
