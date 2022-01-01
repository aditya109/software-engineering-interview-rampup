# Binary Tree Path Sum

## Problem

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

```
Input: root = [1,2,3], targetSum = 5
Output: false
```

**Example 3:**

```
Input: root = [1,2], targetSum = 0
Output: false
```

 

## Solution 

**Pseudocode**

```pseudocode
Function hasPathSum
	Pass In: root, targetSum
	if root == None:
		return False
	if root.left != None and root.right != None and root.val == targetSum
		return True
	targetSum -= root.val
	return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)
	Pass Out: bool
```

