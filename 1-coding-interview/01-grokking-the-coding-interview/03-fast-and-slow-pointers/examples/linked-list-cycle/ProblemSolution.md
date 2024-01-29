# Linked List Cycle

## Problem

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

Can you solve it using `O(1)` (i.e. constant) memory?

**Example 1:**

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

**Example 3:**

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

## Solution 

*Naïve Approach:*

Use Hash Table to mimic a graph and check if value exists for the current node or not.

*Efficient Solution:*

Using fast and slow pointers

```
3 👉 2 👉 0 👉 4
  👆            👇
  👆            👇
   👈👈👈👈👈👈  
```



**Pseudocode**

```pseudocode
Function problemName
	Pass In: head 
	slow = head
	fast = head
	while fast is not None and fast.next is not None
		fast = fast.next.next
		slow = slow.next
		if slow == fast
			return True
	Pass Out: False
```

