from collections import defaultdict
from heapq import *


def dijkstra(graph, src, dest):

    # make a graph with edges
    g = defaultdict(list)
    for left, right, cost in edges:
        g[left].append((cost, right))

    q = [(0, src, ())]  # (cost, v1, path)
    visited = set()
    mins = {src: 0}

    while q:
        (cost, v1, path) = heappop(q)  # we have min heap top element

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
print(dijkstra(edges, "A", "E"))
print("===========================")
print("F -> G:")
print(dijkstra(edges, "F", "G"))
print("===========================")


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
