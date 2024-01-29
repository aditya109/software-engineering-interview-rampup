# Triplets with Smaller Sum

Given an array of n integers nums and a target, find the number of index triplets `i`, `j`, `k` with `0 <= i < j < k < n`

that satisfy the condition `nums[i] + nums[j] + nums[k] < target`.

```
For example, given nums = [-2, 0, 1, 3], and target = 2.
Return 2. Because there are two triplets which sums are less than 2:
- [-2, 0, 1]
- [-2, 0, 3]
```

## Solution:

**Pseudocode**: O(N<sup>2</sup>)

```pseudocode
function getTripletWithSmallerSum(nums, target)
	tripletCount = 0
	sort(nums)
	for index in range(length(num)-2)
		windowStart = index + 1
		windowEnd = length(nums) - 1
		currentSum = 0
		
		while windowStart < windowEnd
			currentSum = nums[index] + nums[windowStart] + nums[windowEnd]
			if currentSum < target
            	tripletCount += windowEnd - windowStart 
            	windowStart += 1
            else
            	windowEnd -= 1
    return tripletCount
```




