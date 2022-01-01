# Graph BFS

```python
from queue import Queue
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
"""
visited = {
    A B C D E F 
}
q = {
    C D E
}
"""

def bfs(graph, s):
    q = Queue()
    q.put(s)
    visited = set()
    while not q.empty():
        node = q.get()
        print(node, end=" ")
        if node not in visited:
            visited.add(node)
        for connected_node in graph[node]:
            if connected_node not in visited:
                q.put(connected_node)
                visited.add(connected_node)
            

bfs(graph, 'A')

```

## Graph DFS

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()  # Set to keep track of visited nodes


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


dfs(visited, graph, 'A')
```

