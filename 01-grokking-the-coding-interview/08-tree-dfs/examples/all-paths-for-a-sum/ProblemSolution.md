# All Paths for a Sum

## Problem

Given the `root` of a binary tree and an integer `targetSum`, return all **root-to-leaf** paths where each path's sum equals `targetSum`.

A **leaf** is a node with no children.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg)

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

```
Input: root = [1,2,3], targetSum = 5
Output: []
```

**Example 3:**

```
Input: root = [1,2], targetSum = 0
Output: []
```

## Solution 

**Pseudocode**

```pseudocode
Function dfs
	Pass In: root, targetSum, sumOfCurrentPath, currentPath, result
	if root == None
		return None
	sumOfCurrentPath += root.val
    if root.left != None and root.right != None and sumOfCurrentPath == targetSum
    	result.append([*currentPath, root.val])
    	return None
    currentPath.append(root.val)
    dfs(root.left, targetSum, sumOfCurrentPath, currentPath, result)
    dfs(root.right, targetSum, sumOfCurrentPath, currentPath, result)
    sumOfCurrentPath -= root.val
    currentPath.pop()
	Pass Out: None
	
Function pathsSum
	Pass In: root, targetSum
	result = []
	currentPath = []
	sumOfCurrentPath = 0
	dfs(root, targetSum, sumOfCurrentPath, currentPath, result)
	Pass Out: result
```

