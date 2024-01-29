# Zigzag Traversal

## Problem

Given the `root` of a binary tree, return *the zigzag level order traversal of its nodes' values*. (i.e., from left to right, then right to left for the next level and alternate between).

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
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
Function zigzagLevelOrder
	Pass In: root
	if root == None
		return []
	else
		q = Queue()
		q.enqueue((root, 0))
		nodesInCorrespondingLevel = []
		nodesInCurrentLevel = []
		currentLevel = []
		
		while not isEmpty(q)
			(element, level) = q.deque()
			if currentLevel == level
            	if level % 2 != 0
                	nodes_in_current_level.insert(0, element.val)
                else
					nodesInCurrentLevel.append(element.val)
			else
				nodesInCorrespondingLevel.append(nodesInCurrentLevel)
				nodesInCurrentLevel = [element.val]
				currentLevel += 1
            if element.left != None
                q.enqueue((element.left, level + 1))
            if element.right != None
                q.enqueue((element.right, level + 1))
        nodesInCorrespondingLevel.append(nodesInCurrentLevel)
	Pass Out:nodesInCorrespondingLevel
```

