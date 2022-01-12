import sys


class MainApp:
    def __init__(self):
        pass
    '''
    Find the max sum of subarray of a fixed size 3
    Example input:
    [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    === 16
    '''
    def run(self, arr, k):
        max_value = -sys.maxsize - 1
        current_running_sum = 0

        for idx, ele in enumerate(arr):
            current_running_sum += arr[idx]

            if idx >= k - 1:
                max_value = max(current_running_sum, max_value)
                current_running_sum -= arr[idx - (k - 1)]
        return max_value
