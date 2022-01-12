# Right View of Binary Tree

## Problem

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

**Example 2:**

```
Input: root = [1,null,3]
Output: [1,3]
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
Function rightViewBinaryTree
	Pass In: root
	if root is None
		return root
	else
		q = Queue()
		q.enqueue((root, 0))
		currentLevel = 0
		rightViewNodes = []
		rightMostNode = root.val
		while isEmpty(q) != True
			(node, level) = q.deque()
        	if currentLevel != level
        		rightViewNodes.append(rightMostNode)
        		currentLevel += 1
        	rightMostNode = node.val
        
        
        	if node.left != None
            	q.enqueue((node.left, level+1))
            else
	            q.enqueue((node.right, level+1))
        rightViewNodes.append(rightMostNode)
	Pass Out:rightViewNodes
```

