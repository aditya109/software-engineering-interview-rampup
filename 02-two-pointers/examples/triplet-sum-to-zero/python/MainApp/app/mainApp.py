import sys


class MainApp:
    def __init__(self):
        pass
    '''
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

    Notice that the solution set must not contain duplicate triplets.

    Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Example 2:

    Input: nums = []
    Output: []
    Example 3:

    Input: nums = [0]
    Output: []
    
    '''

    def run(self, nums):
        result = list()
        nums.sort()
        for index in range(len(nums)-2):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            window_start = index + 1
            window_end = len(nums) - 1
            while window_start < window_end:
                current_sum = nums[index] + \
                    nums[window_end] + nums[window_start]
                if current_sum < 0:
                    window_start += 1
                elif current_sum > 0:
                    window_end -= 1
                else:
                    result.append(
                        [nums[index], nums[window_start], nums[window_end]])
                    while window_start < window_end and nums[window_start] == nums[window_start + 1]:
                        window_start += 1
                    while window_start < window_end and nums[window_end] == nums[window_end-1]:
                        window_end -= 1
                    window_end -= 1
                    window_start += 1
        return result
