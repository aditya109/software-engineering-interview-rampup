# Database types and comparison


ACID databases choose consistency.

| Letter          | Meaning                                              |
| --------------- | ---------------------------------------------------- |
| **A**tomicity   | Either all transactions would be successful or none. |
| **C**onsistency | Measurement of correctness.                          |
| **I**solation   | Transaction execution should be independent.         |
| **D**urability  | Persistence of Data                                  |

BASE databases choose availability.

| Letter                      | Meaning                                                   |
| --------------------------- | --------------------------------------------------------- |
| **B**asically **A**vailable | Available in multiple failures.                           |
| **S**oft state              | State of system may change over time, even without input. |
| **E**ventual consistency    | Eventual data convergence.                                |

| Topic         | SQL                                                          | NoSQL                                                        |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| *Storage*     | Stores data in tables.                                       | Have different data storage models.                          |
| *Schema*      | Each record conforms to a <span style="color:orange">**fixed schema**</span>. Schema can be altered but with modifying the whole database. | Schemas are <span style="color:orange">**dynamic**</span>.   |
| *Querying*    | Use SQL for defining and manipulating the data.              | Queries are focused on a collection of documents. UnQL (unstructured query language) is used. Different databases have different syntax. |
| *Scalability* | Vertical scaling is expensive. Horizontal scaling is time-consuming. | Horizontal scaling is cheap.                                 |
| *ACID*        | ACID compliant, data is reliable, guarantee of transactions. | Most sacrifice ACID for performance and scalability.         |
| *Examples*    | Instagram, Stack Overflow, YouTube                           |                                                              |

## NoSQL databases

1. **Key-value store-type**: Redis, [Voldemort](https://www.project-voldemort.com/), DynamoDB.
2. **Document-type**: CouchDB, MongoDB.
   - Document-stored data.
   - Collection grouped docs.
   - Each document can have different structure.
3. **Wide columnar-type**: Cassandra, HBase (compression, in-memory optimization, filters on a column base).
   - Columnar families.
   - Container for rows.
   - Each rows can be different columns.
4. **Graph-type**: Neo4J, InfiniteGraph.

## Characteristics of NoSQL databases

The insertions and retrieval are in form of full objects.

| Pros                                 | Cons                              |
| ------------------------------------ | --------------------------------- |
| Full object insertion and retrieval  | Not built for update              |
| Schema is flexible                   | Consistency is a problem here.    |
| Read times are comparatively slower. | Built-in horizontal partitioning. |
| Metrics/Aggregation is facilitated.  | Joins are not implicit.           |

### Cassandra - inner working

