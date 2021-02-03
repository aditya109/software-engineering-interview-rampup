import sys


class MainApp:
    def __init__(self):
        pass

    def run(self, arr, k):
        max_value = -sys.maxsize - 1
        current_running_sum = 0

        for idx, ele in enumerate(arr):
            current_running_sum += arr[idx]

            if idx >= k - 1:
                max_value = max(current_running_sum, max_value)
                current_running_sum -= arr[idx - (k - 1)]
        return max_value
