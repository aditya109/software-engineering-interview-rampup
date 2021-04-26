# Sum Root to Leaf Numbers

## Problem

You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

- For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return *the total sum of all root-to-leaf numbers*.

A **leaf** node is a node with no children.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg)

```
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg)

```
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

 

## Solution 

**Pseudocode**

```pseudocode
Function sumRootToLeaves
	Pass In: root
	if root is None
		return 0
	if root.left is None and root.right is None
		return int(root.val)
	if root.left is not None
		root.left.val = 10*root.val + root.left.val
    if root.right is not None
		root.right.val = 10*root.val + root.right.val
	Pass Out: sumRootToLeaves(root.left) + sumRootToLeaves(root.right)
```

