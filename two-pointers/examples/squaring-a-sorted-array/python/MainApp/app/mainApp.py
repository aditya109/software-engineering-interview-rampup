import sys


class MainApp:
    def __init__(self):
        pass
    '''
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

    Example 1:

    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
    Example 2:

    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]
 
    '''
    '''
                -7 -3 2 3 11
                 ^
                           ^
                         121
    '''

    def run(self, nums):
        window_end = len(nums) - 1
        window_start = 0

        result = []

        while window_start <= window_end:
            if abs(nums[window_start]) < abs(nums[window_end]):
                result.append(nums[window_end]*nums[window_end])
                window_end -= 1
            else:
                result.append(nums[window_start]*nums[window_start])
                window_start += 1
        return result[::-1]



