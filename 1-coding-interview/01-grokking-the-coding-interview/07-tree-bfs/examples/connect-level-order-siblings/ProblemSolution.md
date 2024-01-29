# Connect Level Order Siblings 

## Problem

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

 

**Follow up:**

- You may only use constant extra space.
- Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/02/14/116_sample.png)

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

 

## Solution 

**Pseudocode**

```pseudocode
Function levelAverage
	Pass In: root
	if root is None
		return root
	else
		q = Queue()
		q.enqueue((root, 0))
		tempNode = None
		tempLevel = 0
		while isEmpty(q) != True
			(node, level) = q.deque()
            if tempNone is not None and level == tempLevel
            	tempNode.next = node
            tempNode, tempLevel = node, level
            if node.left != None
            	q.enqueue((node.left, level+1))
            else
	            q.enqueue((node.right, level+1))
        
	Pass Out:root
```

```pseudocode
Function levelAverage
	Pass In: root
	
	Pass Out:root
```

