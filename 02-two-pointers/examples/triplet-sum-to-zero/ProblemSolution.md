# Triplet Sum to Zero

Given an array `nums` of *n* integers, are there elements *a*, *b*, *c* in `nums` such that *a* + *b* + *c* = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

**Example 1:**

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2:**

```
Input: nums = []
Output: []
```

**Example 3:**

```
Input: nums = [0]
Output: []
```

## Solution:

**Pseudocode**: O(N<sup>2</sup>)

```pseudocode
function threeSum(nums)
	result = list()
	sort(nums)
	
	for index in range(length(nums)-2)
		if index > 0 and nums[index] == nums[index-1] 
			// when index = 0, we skip the the duplicacy check as we do not have the previous element to compare it with
			continue
		windowStart = index + 1
		windowEnd = length(nums)-1
		while windowStart < windowEnd
			currentSum = nums[index] + nums[windowStart] + nums[windowEnd]
			
			if currentSum < 0
				windowStart +=1
			else if currentSum > 0
				windowEnd -= 1
			else
				add list(nums[index], nums[windowStart], nums[windowEnd]) to result
				while windowStart < windowEnd and nums[windowStart] == nums[windowStart+1]
				// again skip the the duplicacy check
					windowStart += 1
				while windowStart < windowEnd and nums[windowEnd] == nums[windowEnd-1]
				// again skip the the duplicacy check
					windowEnd -= 1
				windowEnd -= 1
				windowStart += 1
	return result
```



