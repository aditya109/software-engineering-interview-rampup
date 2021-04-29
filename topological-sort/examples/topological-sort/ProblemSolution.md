# Topological Sort

## Problem

Implement topological sort.

## Solution 



**Pseudocode**

```pseudocode
visited = set()
outputStack = []
function dfs:
	Pass In: graph, node
	if node not in visited
		visited.add(node)
		for neighbour in graph[node]
			dfs(graph, neighbour)
		outputStack.insert(0, node)
	Pass Out: None
function topsort(graph):
	Pass In: graph
	for node in graph
		dfs(graph, node)
	Pass Out: None
```

