def bellman_ford(nodes, edges, source_index=0):
    # fill the distance array
    path_lengths = {v: float("inf") for v in nodes}
    path_lengths[source_index] = 0

    # fill the predecessor array
    paths = {v: [] for v in nodes}
    paths[source_index] = [source_index]

    # relax edge by |V| -1
    for _ in range(len(nodes) - 1):
        for (u, v), w in edges.items():
            if path_lengths[u] + w < path_lengths[v]:
                path_lengths[v] = path_lengths[u] + w
                paths[v] = paths[u] + [v]

    # detect negative cycle
    # if the value changes we have a negative cycle in the graph
    # and we cannot find the shortest distances
    for (u, v), w in edges.items():
        if path_lengths[u] + w < path_lengths[v]:
            print("negative cycle in graph")
            return
    # No negative weight cycle found!
    # Print the distance and predecessor array
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
