# Binary Tree Level Order Traversal

## Problem

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
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

Solution name

**Pseudocode**

```pseudocode
Function levelOrderTraversal
	Pass In: root
	if root is None
		return []
	else
		q = Queue()
		q.enqueue((root, 0))
		nodesCorrespondingToLevels = []
		nodesInCurrentLevel = []
		currentLevel = 0
		while isEmpty(q) != True
			(node, level) = q.deque()
            if currentLevel == level
            	add node -> nodesInCurrentLevel
            else
            	add nodesInCurrentLevel -> nodesCorrespondingToLevels
            	nodesInCurrentLevel = [node.val]
            	currentLevel += 1
            if node.left != None
            	q.enqueue((node.left, level+1))
            else
	            q.enqueue((node.right, level+1))
        add nodesInCurrentLevel -> nodesCorrespondingToLevels
	Pass Out:nodesCorrespondingToLevels
```

