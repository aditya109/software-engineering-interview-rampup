package mainapp

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
	var length, interimSum int
	length = 0
	interimSum = 0

	for i := 0; i < len(nums); i++ {
		interimSum += nums[i]

		if interimSum > target {
			// do something, as interim sum is much much greater than target
		} else {
			// do something, if interim sum is less than target
		}
	}

	return length
}
