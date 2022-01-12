# Reverse Level Order Traversal

## Problem

Given the `root` of a binary tree, return *the bottom-up level order traversal of its nodes' values*. (i.e., from left to right, level by level from leaf to root).

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
```

**Example 2:**

```
Input: root = [1]
Output: [[1]]
```

**Example 3:**

```
Input: root = []
Output: []
```

## Solution 

**Pseudocode**

```pseudocode
Function levelOrderBottom
	Pass In: root
	if root is None
		return []
	q = Queue()
	q.enqueue((root, 0))
	
	currentLevel = 0
	nodesInCorrespondingLevels = Fifo()
	nodesInCurrentLevel = list()
	while isEmpty(q) != True
		(node,level) = q.deque()
		
		if currentLevel == level
			nodesInCurrentLevel.append(node.val)
		else
			nodesInCorrespondingLevels.push(nodesInCurrentLevel)
			nodesInCurrentLevel = [node.val]
			currentLevel += 1
        if root.left:
        	q.enqueue((node.left, level + 1))
        if root.right:
        	q.enqueue((node.right, level + 1))
    nodesInCorrespondingLevels.push(nodesInCurrentLevel)
	Pass Out:nodesInCorrespondingLevels
```

