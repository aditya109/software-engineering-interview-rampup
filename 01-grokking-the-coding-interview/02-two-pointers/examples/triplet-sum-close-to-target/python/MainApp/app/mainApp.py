import sys


class MainApp:
    def __init__(self):
        pass
    '''
    Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    Example 1:

    Input: nums = [-1, 2, 1, -4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    '''

    def run(self, nums, target) -> int:
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        nums.sort()

        for index in range(len(nums) - 2):
            window_start = index + 1
            window_end = len(nums) - 1

            while window_start < window_end:
                current_sum = nums[index] + \
                    nums[window_start] + nums[window_end]

                if current_sum < target:
                    window_start += 1
                else:
                    window_end -= 1

                if abs(current_sum-target) < abs(result-target):
                    result = current_sum
        return result

