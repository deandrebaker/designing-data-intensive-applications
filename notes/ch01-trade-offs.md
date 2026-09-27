# Ch 1 — Trade-Offs in Data Systems Architecture

## Distillation (closed-book)

<!-- Book shut. 45 minutes. Full sentences, not fragments — a fragment
     can't be wrong, which is how closed-book recall gets faked without
     you noticing. Mark every claim [sure] or [shaky]. -->

### The question this chapter answers

<!-- One sentence. If you can't write it, you didn't get the chapter. -->

What are the main architectural decisions to make when designing a data-intensive system?

### Architectural decisions

#### How does the system process data?

- A system is a collection of interconnected components that work together to achieve a goal.
- A data-intensive system is a system where the primary challenges include data management, which is storing or processing data. The challenges can include large data volumes and high query rates.

##### Operational systems

- Operational systems are used for reading and modifying data based on actions performed by the users.
- Transactional processing is the mechanism used by operational systems to look up, insert, update, and delete small number of records.
- Databases are used to store data for transactional processing. They store entire rows consecutively so that a record can be read from in a single load, and a record can be modified in a single node. This is efficient for transactional processing but inefficient for analytical processing.

##### Analytical processing systems

- Analytical systems are used for performing analytical queries on read-only data.
- Analytical processing is the mechanism used by analytical systems for querying over a huge number of records and calculating agreggate statistics.
- Data warehouses are used to store structured data for analytical processing. They store entire columns consecutively so that many values in a field can be read from in a single load, so the entire field can be read from in less loads than with a database. This is efficient for analytical processing but inefficient for transactional processing.
- Data lakes are used to store unstructured data for analytical processing.
- Data pipelines are used to move data from data sources (usually operational systems) into an analytical system. A reverse data pipeline moves data from analytical systems to an operational system.
- Some analytical systems may share chacteristics of a supercomputing system to increase performance of analytical processing workloads.

##### Hybrid transactional/analytical systems

- Hybrid systems are a middle ground of operational and analytical systems. They provide a common interface for performing transactions and analytical queries, while having separate transactional and analytical processing systems internally. Ideal when an application needs both transactional and analytical processing from the dame data.

#### What does the data represent?

##### Systems of record

- Systems of record hold canonical data, and act as the source of truth for the system. They are normalized to avoid redundancy and maintain data consistency.
- Operational services usually consist of systems of record but may also consist of derived data systems.

##### Derived data systems

- Derived data asystems take data from another system and process it to create derived data. They are denormalized and redundant to improve processing speed.
- Analytical systems are usually derived data systems.
- Derived data systems can be used to integrate data from different systems together.

#### Who manages the hardware for the system?

##### Self-hosted sytems

- Self-hosted systems are maintained by system administrators and can be fine-tuned to handle a specific load. Also, any issues with the system infrastructure can be fixed by the system administrators. However, even when the load of the system decreases, they still cost money to leave on standby. Also, if the load unexpectedly rises past the expected load, the system cannot acquire more resources to meet the demand.

##### Cloud-hosted sytems

- Cloud-hosted systems are maintained by cloud service providers and can automatically allocate/deallocate resources to handle variable load, while being charged proportional to the amount of consumed resources. However, the system cannot be fine-tuned as much as a self-hosted system, and any issues with the cloud infrastructure cannot be addressed by the system maintainers.

#### What environment does the software run in a cloud-hosted system?

##### Virtual machines

- Virtual machines provide an Infrastructure-as-a-Service environment for software to run on, allowing the software access to the operating system. Each machine has an allocated amount of compute, memory, storage, and network bandwidth. Similar to traditional computers but can be provisioned faster and with larger sizes. The consequence is that they need more maintenance and cannot automatically allocate or deallocate resources to support dynamic load. They require developers to build low-level abstractions for interacting with the OS.
- Developers need to focus on capacity planning and performance optimizations to ensure the infrastructure can handle the load.

##### Cloud native services

- Cloud-native systems run on platforms that provide abstractions for compute and storage, allowing the developers to focus on the high-level abstractions instead of building the low-level abstractions. They require less maintenance and can automatically allocate or deallocate resources to support dynamic load or recover from failures. The underlying hardware can be specialized to improve performance. The consequence is that there's less options for fine-tuning the system towards use cases that cloud services aren't optimized for.
- Developers need to focus on financial planning and cost optimizations to save money while using cloud services.

#### What is the structure of the system?

##### Single-node systems

- Single-node systems are simpler to maintain and are simpler to scale to improve performance. However, they cannot solve problems that are inherently distributed. Also, when a component in a single-node system fails, the entire system may fail or need to be stopped so the failing component can be fixed. Also, external communication to the single-node may be bottlenecked by concurrent communication lines, and users that are geographically far away may have higher latency due to the time it takes for messages to be sent and received over a long distance. Also, there's a limit to how much load a single-node system can handle.

##### Distributed systems

- Distributed systems are necessary for problems that are inherently distributed, and allow for redundancy and faster communication by having nodes closer to users. However, they are more complex to maintain due to communication within the system, and there's more points of failure in the communication lines. Communicating between nodes take longer, and troubleshooting is more difficult.
- It's generally preferable to stay with single-node systems and scale them up until they no longer can scale, then switch to a distributed system.

#### How are nodes distributed in a distributed system?

##### Microservices

- Microservices are nodes in a system that provied an interface for interacting with other microservices. Each microservice has a specific job and is usually maintained by their own team in a large organization. Each microservice can be updated independently, but doing this without causing the system to fail may be challenging when other microservices depend on it while it's being updated. Also, microservices are usually still running even when they are not being used so that they are ready to respond to requests.

##### Serverless

- Serverless systems are build on top of Function-as-a-Service services, which can run software while abstracting the infrastructure behind it. It simplifies the management of the infrastructure, and the cost is proportional to the execution time of the software being ran on it. However, FaaS usually has slow start-up times since there's no permanent resource on standby.

### Connections

<!-- What this changes about earlier chapters, about your own builds,
     and about systems you've worked on. -->

- I've spent a lot of time working on operational systems by building websites that act as a system of record, but not much time with building analytical systems
- I did build an ETL pipeline with SSIS in the past, but didn't know it was moving data between databases and data warehouses. I also remember the concept of a data mart being mentioned while working on the project.

### Open questions

<!-- WRITE THESE BEFORE OPENING THE BOOK.
     Things you're unsure of. Highest-value section in the file. -->

- Not sure how transactions actually work. That'll be covered in a later chpater.
- How data is stored in a database vs data warehouse.
- How cloud native systems compare to using VMs.
- Identifying when a problem is inherently distributed.

## What I got wrong

<!-- Only after the above is done. 45 minutes. Open the book and correct
     yourself here. Each correction cites the chapter and heading it
     came from. While the book is open, copy this chapter's headings
     into plan/toc.md.

     Watch for two kinds:
       - [shaky] that turned out right — you know more than you think
       - [sure] that turned out wrong — the dangerous kind; raw
         correctness hides these completely

     /close moves every correction into review/queue.md. -->

- I didn't fully understand what an operational system is and how it relates to OLTP and systems of record.
- I didn't fully understand what an analytical system is and how it relates to OLAP and derived data system.
- I forgot how HTAP works.
- Forgot about serverless architecture.
- Didn't remember the pros and cons of VMs vs Cloud-Native systems.
- I was mixing up single-node and supercomputing systems together.
