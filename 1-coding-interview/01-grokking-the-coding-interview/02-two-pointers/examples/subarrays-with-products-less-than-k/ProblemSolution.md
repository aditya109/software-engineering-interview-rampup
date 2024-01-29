# Subarray Product Less Than K

Your are given an array of positive integers `nums`.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than `k`.

**Example 1:**

```
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```

## Solution

**Pseudocode**: O(N<sup>2</sup>)

```pseudocode
function numSubarrayProductLessThanK(nums, target)
	windowStart = 0
	windowEnd = length(nums) - 1
	if target <= 1
		return 0
	subarraysCount = 0
	product = 1
	for windowEnd, element in enumerate(nums)
		product = product * element
		while product >= target
			product = product // element
			windowStart += 1
		subarraysCount += windowEnd - windowStart + 1
	return subarraysCount
```

