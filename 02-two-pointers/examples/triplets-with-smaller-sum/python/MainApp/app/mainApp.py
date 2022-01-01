import sys


class MainApp:
    def __init__(self):
        pass
    '''
    Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

    For example, given nums = [-2, 0, 1, 3], and target = 2.
    Return 2. Because there are two triplets which sums are less than 2:
    [-2, 0, 1]
    [-2, 0, 3]
    '''

    def run(self, nums, target):
        triplet_count = 0
        nums.sort()

        for index in range(len(nums)-2):
            window_start = index + 1
            window_end = len(nums) - 1
            current_sum = 0

            while window_start < window_end:
                current_sum = nums[index] + \
                    nums[window_start] + nums[window_end]

                if current_sum < target:
                    triplet_count += window_end-window_start
                    window_start += 1
                else:
                    window_end -= 1
        return triplet_count


