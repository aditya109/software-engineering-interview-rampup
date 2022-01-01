# Reorder List

## Problem

You are given the head of a singly linked-list. The list can be represented as:

```
L0 → L1 → … → L(n - 1) → Ln
```

*Reorder the list to be on the following form:*

```
L0 → Ln → L1 → L(n - 1) → L2 → L(n - 2) → …
```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)

```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

## Solution 

Solution name

**Pseudocode**

```pseudocode
Function reorderList
	Pass In: head
	if head != None or head.next != None
		return head
	
	# find the middle of the linked list
	slow = fast = head
	while fast != None and fast.next != None
		slow = slow.next
		fast = fast.next.next
	
	# reverse the second half
	reversedHalf = None
	
	while slow != None
		temp = slow.next
		slow.next = reversedHalf
		reversedHalf = slow
		slow = temp
	
	# merge the two lists
	headFront, headBack = head, reversedHalf
	
	# we want to skip the last element because the last node of reversedHalf is duplicate 
	while headBack.next != None
		nextHopFront = headFront.next
		nextHopBack = headBack.next
		
		headFront.next = headBack
		headBack.next = nextHopFront
		
		headFront = nextHopFront
		headBack = nextHopBack
	
	Pass Out: head
```

