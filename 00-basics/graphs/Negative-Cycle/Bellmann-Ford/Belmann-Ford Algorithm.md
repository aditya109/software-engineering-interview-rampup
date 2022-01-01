# Belmann-Ford Algorithm

- Single Source Shortest Path.

- Graph with negative edge weight cycle.

  > Dijkstra can' detect if graph has *negative edge weight cycle*, while Belmann-Ford can.
  > A *negative edge weight cycle* is a cycle whose accumulative weight is *negative*.

- Time complexity = **O(V*E)**

**Undirected Graph**

Belmann-Ford will definitely work if all edges in an undirected graph are positive.

> Belmann-Ford doesn't find shortest path for undirected graph if it has any negative edge.

1. Initialize all vertices at `dist` = infinity except source (O).
2. Relax all E edges (V-1) times.
   If d[u] + cost(u,v) < d[V] then d[v] = d[u] + cost(u,v)
   else SKIP
3. Relax once more. If we find a new shortest path for any node then we have negative edge cycle, else we don't.