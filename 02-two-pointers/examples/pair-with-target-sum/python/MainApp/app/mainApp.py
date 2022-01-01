import copy


class MainApp:
    def __init__(self):
        pass
    '''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].

    [3, 2, 4]

    '''

    def run(self, nums, target):
        start_pointer = 0
        end_pointer = len(nums) - 1

        while start_pointer < end_pointer:
            if nums[start_pointer] + nums[end_pointer] == target:
                return [start_pointer, end_pointer]
            elif nums[start_pointer] + nums[end_pointer] < target:
                start_pointer += 1
            else:
                end_pointer -= 1

        return []

