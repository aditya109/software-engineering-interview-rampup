# Minimum Spanning Tree

A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a **connected, edge-weighted undirected graph** that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

For the given graph,

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Fig-0-300x139.jpg)

we have the following minimum spanning tree.

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/fig8new.jpeg)

> Note:
>
> - All the nodes must be connected to form a spanning tree.

## Prim's Algorithm

Prim's is a greedy MST algorithm that works well on dense graphs. On these graphs, Prim's meets or improves on the time bounds of its popular rivals.

However, when it comes to finding the **minimum spanning forest** on a disconnected graph, Prim's cannot do this as easily.

The **lazy version** of Prim's has a runtime of `O(E*log(E))`, but the **eager version** has a better runtime of `O(E*log(V))`.

We use adjacency list for 

### 







































## Kruskal's Algorithm

    1. Sort all the edges in non-descending order of their weights.
    2. i) Pick the smallest edge.
      ii) Check if the new edge forms a cycle in our spanning tree being formed.
      iii) If cycle is not formed, include the edge, otherwise, discard the edge.
    3. Repeat step 2 unless `v-1` edges are included in minimum spanning tree.

## Time Complexity

`O(E log E + E log V)`

`E log E` - sorting E edges
`E log V` - Disjoint set union find on E edges



