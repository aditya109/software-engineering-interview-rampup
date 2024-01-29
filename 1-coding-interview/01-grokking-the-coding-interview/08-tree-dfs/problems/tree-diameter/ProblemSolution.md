# Tree Diameter

## Problem

Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**

```
Input: root = [1,2]
Output: 1
```

 

## Solution 

**Pseudocode**

```pseudocode
ans = 0
Function findDepth:
	Pass In: node
	if node is None
		return 0
	leftSubtreeDepth = findDepth(node.left)
	rightSubtreeDepth = findDepth(node.right)
	ans = max(ans, leftSubtreeDepth + rightSubtreeDepth)
	Pass Out: 1 + max(leftSubtreeDepth, rightSubtreeDepth)

Function findTreeDiameter
	Pass In: root
	ans = 0
	findDepth(root)
	Pass Out: ans
```

