# Indexes

## Why thou ? 😕

1. It improves the performance of search analysis.
2. Decreases the write performance and increased storage overhead which applied to insert, update and delete operation.

| Column<sub>1</sub> | Column<sub>2</sub> (Indexing applied here) | Column<sub>3</sub> | Column<sub>4</sub> |
| ------------------ | :----------------------------------------: | ------------------ | ------------------ |
|                    |                xxxxxxxxxxx                 |                    |                    |
|                    |                xxxxxxxxxxx                 |                    |                    |
|                    |                xxxxxxxxxxx                 |                    |                    |

TODO:

There are two types of indexing:

1. **Ordered indexing** - ascending order
2. **Hash indexing** - hash function

## Where thou ? 🤨

1. Indexing should not be used on small tables.
2. It should not be used on columns which return high percentage of data rows when used with a filter.
3. It should not be used on columns that contain a high number of null values.
4. It should not be used on columns which get changed frequently.