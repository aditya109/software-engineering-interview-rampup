# Tree BFS

All connections connected to a node is checked at one time.

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif)

```
BFS of above Tree

Breadth First Traversal : 1 2 3 4 5
```

```pseudocode
FUNCTION traverseTreeInBFS
	passIn: root
	if root == None
		return
	queue = Queue()
	queue.enqueue(root)
	while isEmpty(queue) == False
		e = queue.deque()
		print(e)
		
		if e.left != None:
			queue.enqueue(e.left)
		if e.right != None:
			queue.enqueue(e.right)
	passOut: None
```

