# Reverse Nodes in k-Group

## Problem

Given a linked list, reverse the nodes of a linked list *k* at a time and return its modified list.

*k* is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of *k* then left-out nodes, in the end, should remain as it is.

**Follow up:**

- Could you solve the problem in `O(1)` extra memory space?
- You may not alter the values in the list's nodes, only nodes itself may be changed.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

**Example 3:**

```
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
```

**Example 4:**

```
Input: head = [1], k = 1
Output: [1]
```

[Reverse Nodes in k-Group - LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## Solution 

**Pseudocode**

```pseudocode
Function getListLength
	Pass In: head 
	if head is None
		return length
	
	Pass Out: getListLength(node.next, length+1)

Function reverseKGroup
	Pass In: head, k
	if head is not None or k == 1
		return head
	length = getListLength(head)
	
	prev = None
	curr = head
	while length >= k
		connection = prev
		tail = curr
		temp = k
        while temp > 0:
        	nextNode = curr.next
        	curr.next = prev
        	prev = curr
        	curr = nextNode
        	temp -= 1
        if connection is not None
        	connection.next = prev
        else
        	head = prev
        prev = tail
        tail.next = curr
		length -= k
	Pass Out: head
```

