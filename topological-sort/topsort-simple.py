graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

def top_sort(graph):
    n = len(list(graph.keys()))
    v = [False] * n
    ordering = [0] * n
    i = n - 1

    for at in range(n):
        if v[at] == False:
            visitedNodes = set()
            dfs(visitedNodes, graph, at )
            for nodeId in visitedNodes:
                ordering[i] = nodeId
                i = i - 1 

top_sort(graph)
