# Squares of a Sorted Array

Given an integer array `nums` sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

**Example 1:**

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

**Example 2:**

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

## Solution:

**Pseudocode**: O(N)

```pseudocode
function squaresOfSortedArray(nums)
	windowEnd = length(nums) - 1
	windowStart = 0
	
	result = list()
	
	while windowStart <= windowEnd
		if absoluteValue(nums[windowStart]) < absoluteValue(nums[windowEnd])
			append nums[windowEnd]^2 to the end of nums
			windowEnd += 1
		else
			append nums[windowStart]^2 to the end of nums
			windowStart += 1
	return reverseList(result)
```



