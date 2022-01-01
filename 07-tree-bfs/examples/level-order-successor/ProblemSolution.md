# Level Order Successor

## Problem

Given a binary tree and a node in the binary tree, find level order successor of the given node. That is, the node that appears after the given node in the level order traversal of the tree.

**Note**: The task is not just to print the data of the node, you have to return the complete node from the tree.

**Examples**:

```
Consider the following binary tree
              20            
           /      \         
          10       26       
         /  \     /   \     
       4     18  24    27   
            /  \
           14   19
          /  \
         13  15

Levelorder traversal of given tree is:
20, 10, 26, 4, 18, 24, 27, 14, 19, 13, 15

Input : 24
Output : 27

Input : 4
Output : 18
```

## Solution 

Solution name

**Pseudocode**

```pseudocode
Function levelOrderSuccessor
	if root is None
		return []
	else
		q = Queue()
		q.enqueue(root)
		isKeyFound = False
		while isEmpty(q) != True
			node = q.deque()
            
            if isKeyFound
            	return node
            if node.val == key:
            	isKeyFound = True
            
            if node.left != None
            	q.enqueue(node.left)
            else
	            q.enqueue(node.right)
	Pass Out:None
```

