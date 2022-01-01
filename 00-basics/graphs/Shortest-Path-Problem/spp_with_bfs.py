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
