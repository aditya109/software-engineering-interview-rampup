# Average of Levels in Binary Tree

## Problem

Given the `root` of a binary tree, return *the average value of the nodes on each level in the form of an array*. Answers within `10-5` of the actual answer will be accepted.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg)

```
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
```

 

## Solution 

Solution name

**Pseudocode**

```pseudocode
Function levelAverage
	if root is None
		return []
	else
		q = Queue()
		q.enqueue((root, 0))
		averageNodeValueCorrespondingToLevel = []
		nodesInCurrentLevel = []
		currentLevel = 0
		while isEmpty(q) != True
			(node, level) = q.deque()
            if currentLevel == level
            	add node -> nodesInCurrentLevel
            else
            	add sum(nodesInCurrentLevel)/len(nodesInCurrentLevel) -> averageNodeValueCorrespondingToLevel
            	nodesInCurrentLevel = [node.val]
            	currentLevel += 1
            if node.left != None
            	q.enqueue((node.left, level+1))
            else
	            q.enqueue((node.right, level+1))
        add sum(nodesInCurrentLevel)/len(nodesInCurrentLevel) -> averageNodeValueCorrespondingToLevel
	Pass Out:nodesCorrespondingToLevels
```

