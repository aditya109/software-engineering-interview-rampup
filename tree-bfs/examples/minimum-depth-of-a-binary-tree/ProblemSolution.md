# Minimum Depth of Binary Tree

## Problem

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:** A leaf is a node with no children.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: 2
```

**Example 2:**

```
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
```

 

## Solution 

**Pseudocode**

```pseudocode
Function minimumDepthBinaryTree
	Pass In: root
	if root is None
		return 0
	else
		q = Queue()
		q.enqueue((root, 0))
		while isEmpty(q) != True
			(node, level) = q.deque()
			if node.left is None and node.right is None
				return level + 1
			if node.left != None
            	q.enqueue((node.left, level+1))
            else
	            q.enqueue((node.right, level+1))
        
	Pass Out:Nones
```

