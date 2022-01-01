# 3Sum Closest

Given an array `nums` of *n* integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

**Example 1:**

```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

## Solution:

**Pseudocode**: O(N<sup>2</sup>)

```pseudocode
function threeSumClosest(nums, target)
	result = nums[0] + nums[1] + nums[length(nums)-1]
	sort(nums)
	
	for index in range(length(nums)-2)
		windowStart = index + 1
		windowEnd = length(nums) - 1
		currentSum = 0
		while windowStart < windowEnd
			currentSum = nums[index] + nums[windowStart] + nums[windowEnd]
			if currentSum < target:
				windowStart += 1
			else
				windowEnd -= 1
			if absoluteValue(currentSum - target) < absoluteValue(result - target)
				result = currentSum
	return result		
		
```



