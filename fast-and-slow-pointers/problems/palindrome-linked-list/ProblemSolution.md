# Palindrome Linked List

## Problem

Given the `head` of a singly linked list, return `true` if it is a palindrome.

Could you do it in `O(n)` time and `O(1)` space?

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

```
Input: head = [1,2,2,1]
Output: true
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)

```
Input: head = [1,2]
Output: false
```

## Solution 

**Pseudocode**

```pseudocode
Function isPalindrome
	Pass In: head
	find the middle node
	reverse the second half
	compare the first and second half
		if match fails return False
	Pass Out: True
```

