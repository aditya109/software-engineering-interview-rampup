# Shortest Path Problem

## using BFS

BFS runs with a time complexity of `O(V+E)` and is very useful for finding **the shortest path of unweighted graphs**.

A BFS starts at some arbitrary node of a graph and explores the neighbour nodes first, before moving to the next level neighbours.

```python
from queue import Queue

graph = {
    0: [7, 9, 11],
    1: [10, 8],
    2: [12, 3],
    3: [2, 3, 4],
    4: [3],
    5: [],
    6: [5, 7],
    7: [0, 3, 6, 11],
    8: [1, 9, 12],
    9: [10, 8, 0],
    10: [1, 9],
    11: [7, 0],
    12: [2, 8]
}


def bfs(graph, start_node):
    q = Queue()
    q.put(start_node)

    visited = set()
    predecesor = [None for _ in range(len(graph.keys()))]
    distance = [-1 for _ in range(len(graph.keys()))]
    distance[start_node] = 0
    while not q.empty():
        node = q.get()

        if node not in visited:
            visited.add(node)
        for connected_node in graph[node]:
            if connected_node not in visited:
                q.put(connected_node)
                predecesor[connected_node] = node
                distance[connected_node] = distance[node] + 1

                visited.add(connected_node)
    return predecesor, distance


def reconstruct_path(graph, src, dest, prev):
    path = []
    cur = dest
    while cur != None:
        path.append(cur)
        cur = prev[cur]

    path = path[::-1]

    # if src and e are connected return the path
    if path[0] == src:
        return path
    return []


def finding_shortest_path(graph, start_node, end_node):
    # prev = [None, 10, 3, 7, 3, 6, 7, 0, 9, 0, 9, 0, 8]

    prev, dist = bfs(graph=graph, start_node=start_node)
    return reconstruct_path(graph=graph,
                            src=start_node,
                            dest=end_node,
                            prev=prev), dist


ssp, dist = finding_shortest_path(graph=graph,
                                  start_node=0,
                                  end_node=12)

print(dist)
for index, node in enumerate(ssp[:-1]):
    print("{0} -> {1} by {2} units".format(node,
                                           ssp[index + 1], dist[ssp[index+1]]))
```

## using Dijkstra's Algorithm

Dijkstra runs with a worst case time complexity of O(V<sup>2</sup>) and is very useful for finding the **<u>single shortest path of non-negative weighted graphs</u>**.
Using binary heaps, the time complexity can be reduced to `O((E+V) log V)`, it is only useful when E is low, otherwise if E = V<sup>2</sup>, the time complexity would become V<sup>2</sup>logV.

### Steps

- Maintain a `distance` array where the distance to every node is &#8734;. Mark the distance to the start node `src` to be 0.
- Maintain a Priority Queue `pq` of key-value (node-index, distance) pairs which tell you which node to visit next based on sorted min value.
- Insert `(src, 0)` into the `pq` and loop while `pq` is not empty pulling out the next most promising (node-index, distance) pair.
- Iterate over all edges outwards from the current node and relax each edge appending a new (node-index, distance) key-value pair to the `pq` for every relaxation.

```python
from collection import defaultdict
from heapq import *

def dijkstra(edges, src, dest):
	# make a graph out of edges
    g = defaultdict(list)
    for left, right, cost in edges:
        g[left].append((cost, right))
    
    q = [(0, src, ())] # (cost, v1, path)
    mins = {src:0}
    visited = set()
    
    while q:
        (cost, v1, path) = heappop(q)
        
        if v1 not in visited:
            visited.add(v1)
            
            path = (v1, *path)
            
            if v1 == dest:
                return (cost, path)
            for c, v2 in g.get(v1, ()):
                if v2 in visited:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))
     return float("inf"), None
     
edges = [
    ("A", "B", 7),
    ("A", "D", 5),
    ("B", "C", 8),
    ("B", "D", 9),
    ("B", "E", 7),
    ("C", "E", 5),
    ("D", "E", 15),
    ("D", "F", 6),
    ("E", "F", 8),
    ("E", "G", 9),
    ("F", "G", 11)
]

print("=== Dijkstra ===")
# print(edges)
print("A -> E:")
print_graph(dijkstra(edges, "A", "E"))
print("\n===========================")
print("F -> G:")
print_graph(dijkstra(edges, "F", "G"))
print("\n===========================")

```

```python

def dijkstra_without_heap(nodes, edges, source_index=0):
    adjacent_nodes = {
        v: {} for v in nodes
    }
    for (u, v), w in edges.items():
        adjacent_nodes[u][v] = w

    path_lengths = {
        v: float('inf') for v in nodes
    }
    path_lengths[source_index] = 0

    temporary_nodes = [v for v in nodes]

    while len(temporary_nodes) > 0:
        upper_bounds = {
            v: path_lengths[v] for v in temporary_nodes
        }
        u = min(upper_bounds, key=upper_bounds.get)
        temporary_nodes.remove(u)

        for v, w in adjacent_nodes[u].items():
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + w)
    return path_lengths


e = {
    (0, 1): 1,
    (0, 5): 2,
    (1, 2): 2,
    (1, 5): 2,
    (2, 3): 5,
    (2, 4): 1,
    (4, 3): 4,
    (4, 5): 3,
    (5, 1): 2,
    (5, 2): 3
}
n = [0, 1, 2, 3, 4, 5]
print(dijkstra_without_heap(n, e, 0))
```



## using Bellman-Ford

Bellman-Ford runs with a worst case time complexity of O(EV) and is very useful for finding the **<u>single shortest path of negative weighted graphs</u>**.

> However, Dijkstra's algorithm can fail when the graph has negative edge weights. This is when BF becomes really handy because it can be used to detect **negative cycles** and **determine where they occur**.

![](https://media.geeksforgeeks.org/wp-content/uploads/bellmanford1.png)

- Relax all the edges by V-1 times.

- For vertices pair (u, v), 

  ```
  if d[u] + c[u, v] < d[v]
  	d[v] = d[u] + c[u, v]
  ```

```python
def bellman_ford(nodes, edges, source_index=0):
    # fill the distance array
    path_lengths = {v: float("inf") for v in nodes}
    path_lengths[source_index] = 0

    # fill the predecessor array
    paths = {v: [] for v in nodes}
    paths[source_index] = [source_index]
	
    # 
    for _ in range(len(nodes) - 1):
        for (u, v), w in edges.items():
            if path_lengths[u] + w < path_lengths[v]:
                path_lengths[v] = path_lengths[u] + w
                paths[v] = paths[u] + [v]

    for (u, v), w in edges.items():
        if path_lengths[u] + w < path_lengths[v]:
            print("negative cycle in graph")
            return

    return path_lengths, paths


e = {
    (0, 1): 5,
    (0, 2): 4,
    (1, 3): 3,
    (2, 1): 6,
    (3, 2): 2
}
n = [0, 1, 2, 3]

a, b = bellman_ford(n, e, 0)
print(a)
print(b)

e = {
    (0, 1): -1,
    (0, 5): 2,
    (1, 2): 2,
    (1, 5): -2,
    (2, 3): 5,
    (2, 4): 1,
    (4, 3): -4,
    (4, 5): 3,
    (5, 1): 2,
    (5, 2): 3
}
n = [0, 1, 2, 3, 4, 5]

a, b = bellman_ford(n, e, 0)

print(a)
print(b)
```

## using Floyd-Warshall 

Floyd-Warshall runs with a worst case time complexity of O(V<sup>3</sup>) and is very useful for finding the **<u>all pair shortest path of weighted graphs</u>**.

```python
def floyd_warshall(nodes, edges):
    d = {
        (u, v): float('inf') if u != v else 0 for u in nodes for v in nodes
    }

    for (u, v), cost in edges.items():
        d[(u, v)] = cost
    
    for k in nodes:
        for u in nodes:
            for v in nodes:
                d[(u, v)] = min(d[(u, v)], d[(u, k)] + d[(k, v)])
    if any(d[u, u] < 0 for i in nodes):
        print("Graph has a negative cycle")
    return d



e = {
    (0, 1): 1,
    (0, 5): 2,
    (1, 2): 2,
    (1, 5): 2,
    (2, 3): 5,
    (2, 4): 1,
    (4, 3): 4,
    (4, 5): 3,
    (5, 1): 2,
    (5, 2): 3
}
n = [0, 1, 2, 3, 4, 5]

print(floyd_warshall(n, e))
```

## Comparison of Shortest Path Algorithm

| Algorithms/Traits | Time Complexity  | Space Complexity | Remarks                                      |
| ----------------- | ---------------- | ---------------- | -------------------------------------------- |
| Dijkstra          | O(V log(V) + E)  | O(V)             | no negative-weight edge                      |
| Bellman-Ford      | O(VE)            | O(V)             | negative-weight edge, single source          |
| Floyd-Warshall    | O(V<sup>3</sup>) | O(V<sup>2</sup>) | negative-weight edge, all pair shortest path |









































