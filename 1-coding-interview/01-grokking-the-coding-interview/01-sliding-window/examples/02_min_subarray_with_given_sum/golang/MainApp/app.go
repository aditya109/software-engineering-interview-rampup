package mainapp

import "math"

/*
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [nums_l, nums_l+1, ..., nums_r-1, nums_r] of which the sum is greater than or equal to target.
If there is no such subarray, return 0 instead.
=================================

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
==================================

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
==================================

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
==================================

**/

func Run(nums []int, target int) int {
	n := len(nums)
	minLen := math.MaxInt
	sum, left := 0, 0

	for right := 0; right < n; right++ {
		sum += nums[right]

		for sum >= target {
			minLen = min(minLen, right-left+1)
			sum -= nums[left]
			left++
		}
	}
	if minLen == math.MaxInt {
		return 0
	}
	return minLen
}

func min(a, b int) int {
	return int(math.Min(float64(a), float64(b)))
}
