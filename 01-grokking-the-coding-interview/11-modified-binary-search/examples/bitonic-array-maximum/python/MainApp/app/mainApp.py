class MainApp:
    def __init__(self):
        pass

    '''
    Find the maximum value in a given Bitonic array. 
    An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 
    Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
    
    Example 1:
    Input: [1, 3, 8, 12, 4, 2]
    Output: 12
    Explanation: The maximum number in the input bitonic array is '12'.
    
    Example 2:
    Input: [3, 8, 3, 1]
    Output: 8
    
    Example 3:
    Input: [1, 3, 8, 12]
    Output: 12
    Example 4:
    Input: [10, 9, 8]
    Output: 10
     
    '''

    @staticmethod
    def search(arr, k):
        left, right = 0, len(arr) - 1
        while left <= right:
            # to prevent int overflow
            mid = left + ((right - left) // 2)
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def run(self, arr):
        print(self.search(arr, 1))


MainApp().run([1, 3, 8, 12, 4, 2])
