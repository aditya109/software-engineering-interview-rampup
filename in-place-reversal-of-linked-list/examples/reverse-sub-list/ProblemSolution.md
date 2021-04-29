# Reverse a Sub List

## Problem

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return *the reversed list*.

Could you do it in one pass?

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)

```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

**Example 2:**

```
Input: head = [5], left = 1, right = 1
Output: [5]
```

## Solution 

**Pseudocode**

```pseudocode
Function reverseBetween
	Pass In: head, left, right
	if head is None or left == right
		return head
	curr = head
	prev = None
	while left > 1
		prev = curr
		curr = curr.next
		left -= 1
		right -= 1
	connection = prev
	tail = curr
	
	while right > 0
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
		right -= 1
	if connection is not None:
		connection.next = prev
	else
		head = prev
	tail.next = curr
	Pass Out: head
```

