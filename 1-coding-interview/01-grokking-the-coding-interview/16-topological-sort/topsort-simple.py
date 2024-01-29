gr = {
    'A': ['D'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}

# graph should be DAG
# in top-sort for every u -> v, u will come before v in ordering of the graph
# indegree = incoming edges on the node
# O(V+E)
visited = set()
output_stack = []


def top_sort(graph, start):
    if start not in visited:
        visited.add(start)
        for neighbour in graph[start]:
            top_sort(graph, neighbour)
        output_stack.insert(0, start)


for vertex in gr:
    top_sort(gr, vertex)

for node in output_stack:
    print("{0} -> ".format(node), end="")