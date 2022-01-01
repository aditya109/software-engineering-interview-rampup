# Happy Number

## Problem

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process **ends in 1** are happy.

Return `true` *if* `n` *is a happy number, and* `false` *if not*.

 

**Example 1:**

```
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

**Example 2:**

```
Input: n = 2
Output: false

2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4
```

## Solution 

**Pseudocode**

```pseudocode
Function getDigitsSquareSum
	Pass In: x
	temp_sum = 0
	while x != 0
        temp = t % 10
        temp_sum += (temp * temp)
        t //= 10	
	Pass Out: temp_sum
	
Function isHappyNumber
	Pass In: n
	while n != 1
		n = getDigitsSquareSum(n)
		if n in visited
        	return False
	Pass Out: True
```

