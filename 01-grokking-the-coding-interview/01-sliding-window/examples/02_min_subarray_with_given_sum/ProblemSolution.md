# Minimum Subarray with given Sum

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a **contiguous subarray** `[numsl, numsl+1, ..., numsr-1, numsr]` of which the sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

**Example 1:**

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

**Example 2:**

```
Input: target = 4, nums = [1,4,4]
Output: 1
```

**Example 3:**

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

## Solution:

**Pseudocode** O(n)

```pseudocode
function minimumSubarrayWithGivenSum(arr, targetSum)
	minimumWindowSize = INFINITY
	currentWindowSum = 0
	windowStart = 0
	
	for windowEnd in range(len(arr))
		currentWindowSum += arr[windowEnd]
		
		while currentWindowSum >= targetSum
			minimumWindowSize = minimum(minimumWindowSize, windowEnd - windowStart + 1)
			currentWindowSum -= arr[windowStart]
			windowStart += 1
    return minimumWindowSize == INFINITY ? 0 : minimumWindowSize
```

