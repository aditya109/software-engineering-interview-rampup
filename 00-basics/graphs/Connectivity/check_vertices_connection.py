from queue import Queue
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def areNodesConnected(graph, visited, start_node, end_node):
    visited = set()

    q = Queue()
    q.put(start_node)

    while not q.empty():
        node = q.get()
        if node == end_node:
            return True
        if node not in visited:
            visited.add(node)
        for connected_node in graph[node]:
            if connected_node not in visited:
                q.put(connected_node)
                visited.add(connected_node)
    return False

print(areNodesConnected(graph, set(), 'A', '!F'))
print(areNodesConnected(graph, set(), 'A', 'F'))
