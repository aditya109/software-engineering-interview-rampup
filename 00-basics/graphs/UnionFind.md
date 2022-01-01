# Union Find/Disjoint Set

## Discussion & Examples

### What is Union Find ?

Union Find is a data structure that keeps track of elements which are split into one or more disjoint sets. It has two primary operations:

- `find`
- `union`

### When and where is a Union Find used ?

- `Kruskal's minimum spanning tree algorithm`
- `Grid percolation`
- `Network connectivity`
- `Least Common Ancestor in a Tree`

### Kruskal's minimum spanning tree algorithm

> Given a graph G = (V, E) we wan to find a **Minimum Spanning Tree** in the graph (it may not be unique).
> A minimum spanning tree is a subset of the edges which connect all vertices in the graph with the minimal total edge cost.



### Complexity analysis

|     Operation      | Time Complexity  |
| :----------------: | :--------------: |
|    Construction    |       O(n)       |
|       Union        | α(n) (amortized) |
|        Find        |       α(n)       |
| Get component size |       α(n)       |
| Check if connected |       α(n)       |
|  Count Components  |       O(1)       |



## Implementation Details



### Find & Union Operations

### Path Compression

## Code Implementation