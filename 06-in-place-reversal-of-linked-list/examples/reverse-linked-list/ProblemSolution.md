# Reverse a Linked List

## Problem

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

A linked list can be reversed either iteratively or recursively. Could you implement both?

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**

```
Input: head = []
Output: []
```

## Solution 

Solution name

**Pseudocode**

```pseudocode
Function reverseListIterative
	Pass In: head
	reversedHead = None
	while head
		temp = head.next
		head.next = reversedHead
		reversedHead = head
		head = temp
	Pass Out: reversedHead

Function reverseListRecursive
	Pass In: head, reversedHead=None
	if head is None
		temp = head.next
		head.next = reversedHead
	Pass Out: reverseListRecursive(temp, head)
```

