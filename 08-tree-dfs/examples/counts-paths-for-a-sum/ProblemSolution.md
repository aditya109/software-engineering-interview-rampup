# Counts Paths for a Sum

## Problem

Given the `root` of a binary tree and an integer `targetSum`, return *the number of paths where the sum of the values along the path equals* `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg)

```
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
```

**Example 2:**

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
```

 

## Solution 

**Pseudocode**

```pseudocode
result = 0
Function dfs
	Pass In: root, currentPathSum, targetSum, cache
	if root is None
		return
	currentPathSum += root.val
    oldPathSum = currentPathSum - targetSum
    
    result += cache.get(key = oldPathSum, defaultReturnValue = 0)
    cache[currentPathSum] = cache.get(key = currentPathSum, defaultReturnValue= 0) + 1
    dfs(root.left, currentPathSum, targetSum, cache)
	dfs(root.right, currentPathSum, targetSum, cache)
	cache[currentPathSum] -= 1
	Pass Out: None
	
Function pathSum
	Pass In: root, targetSum
	cache = {0:1}
	currentPathSum = 0
	dfs(root, currentPathSum, targetSum, cache)
	Pass Out: result
```

