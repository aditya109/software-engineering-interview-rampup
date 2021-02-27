import sys


class MainApp:
    def __init__(self):
        pass
    '''
    Given an array `A` of 0s and 1s, we may change up to `K` values from 0 to 1.

    Return the length of the longest (contiguous) subarray that contains only 1s. 

    Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
    Output: 6
    Explanation: 
    [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
    '''

    # def run(self, arr, k):
    #     length = len(arr)
    #     unary_counts = [0, 0]

    #     window_start = 0
    #     maximum_length = 0
    #     maximum_count = 0

    #     for window_end in range(length):
    #         unary_counts[arr[window_end]] += 1
    #         count_of_one = unary_counts[arr[1]]
    #         maximum_count = max(maximum_count, count_of_one)

    #         while window_start <= window_end and unary_counts[0] > k:
    #             unary_counts[arr[window_start]] -= 1
    #             window_start += 1
    #         maximum_length = max(maximum_length, window_end - window_start + 1)
    #     return maximum_length

    def run(self, arr, k):
        window_start = 0

        for window_end in range(len(arr)):
            k -= 1-arr[window_end]

            if k < 0:
                k += 1 - arr[window_start]
                window_start += 1
        return window_end - window_start + 1
