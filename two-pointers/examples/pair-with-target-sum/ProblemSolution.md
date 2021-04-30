# Two Sum

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have **exactly one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**

```
Input: nums = [2,3,4], target = 6
Output: [1,2]
```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Solution:

**Pseudocode**: O(N)

```pseudocode
function isPairSum(A[], arrayLength, targetSum)
	startPointer := 0
	endPointer := arrayLength - 1
	
	while startPointer < endPointer
		if A[i] + A[j] == targetSum
			return True
		else if A[i] + A[j] < targetSum
			startPointer += 1
		else endPointer -= 1
	return False
```

