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