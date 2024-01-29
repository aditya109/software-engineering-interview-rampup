import sys


class MainApp:
    def __init__(self):
        pass
    '''
    /**
    * Find the min subarray length with sum <= 8
    * Example input:
    * [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    * === 1
    */
    '''

    def run(self, arr, target_window_sum):
        minimum_window_size = float('inf')
        current_window_sum = 0
        window_start = 0

        for window_end in range(len(arr)):
            current_window_sum += arr[window_end]

            while(current_window_sum >= target_window_sum):
                minimum_window_size = min(
                    minimum_window_size, window_end-window_start+1)
                current_window_sum -= arr[window_start]
                window_start += 1
        return (minimum_window_size, 0)[minimum_window_size == float('inf')]
