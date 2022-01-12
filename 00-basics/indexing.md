# Indexing

## Types of Indexes:

- Clustered
- Non-clustered
- Column-store
- Spatial
- XML
- Full-text



## What is the difference between Clustered and Non-Clustered Indexes in SQL Server?

| Clustered Index                                              | Non-Clustered Index                                          |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| A clustered index defines the order in which data is physically stored in a table. Table data can be sorted in only one way, therefore there can be only one clustered index per table. | A non-clustered index doesn't sort the physical data inside the table. In fact, it is stored at one place and table data is stored in another place. This allows for more than one non-clustered index per table. |
| In SQL Server, the primary key constraint automatically creates a clustered index on that particular column. | It is instead ordered by the columns that make up the **index**. It stores the data at one location and indices at another location. |
| Cluster index offers faster data accessing.                  | Non-clustered index is slower.                               |
| Clustered index stores data pages in the leaf nodes of the index. | Non-clustered index method never stores data pages in the leaf nodes of the index. |
| The size of the clustered index is quite large.              | The size of the non-clustered index is small compared to the clustered index. |
| A clustered index can improve the performance of data retrieval. | It should be created on columns which are used in joins.     |
|                                                              |                                                              |

> Clustered indexes are faster than non-clustered indexes since they don’t involve any extra lookup step.

### Pros and Cons of Clustered Indexes

| Pros                                                         | Cons                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Clustered indexes are an ideal option for range or group by with max, min, count type queries | A clustered index creates lots of constant page splits, which includes data page as well as index pages. |
| In this type of index, a search can go straight to a specific point in data so that you can keep reading sequentially from there. | Extra work for SQL for inserts, updates, and deletes.        |
| Helps you to minimize page transfers and maximize the cache hits. | A clustered index takes longer time to update records when the fields in the clustered index are changed. |

### Pros and Cons of Non-Clustered Indexes

| Pros                                                         | Cons                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| A non-clustering index helps you to retrieves data quickly from the database table. | A non-clustered index helps you to stores data in a logical order but does not allow to sort data rows physically. |
| Helps you to avoid the overhead cost associated with the clustered index. | Lookup process on non-clustered index becomes costly.        |
| A table may have multiple non-clustered indexes in RDBMS. So, it can be used to create more than one index. | Every time the clustering key is updated, a corresponding update is required on the non-clustered index as it stores the clustering key. |

