# Topological Sort

A topological ordering is an ordering of the nodes in a directed graph where for each directed edge from node A to node B, node A appears before node B in the ordering.

Time complexity : **O(V+E)**

> Topological ordering are not unique.

## Directed Acyclic Graphs (DAG)

Not every graph can have a topological ordering. A graph which contains a cycle cannot have a valid ordering.

The only type of graph which has a valid topological ordering is a **Directed Acyclic Graph(DAG)** (graphs with directed edges and no cycle).

> How do I verify that my graph does not contain a directed cycle?
>
> - One method is to use Tarjan's strongly connected component algorithm which can be used to find these cycles.

By definition, all rooted trees have a topological ordering since they do not contain any cycles.

```
1. Pick an unvisited node.
2. Beginning with the selected node, do a DFS exploring only unvisited nodes.
3. On the recursive callback of the DFS, add the current node to the topological ordering in the reverse order.
```



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



