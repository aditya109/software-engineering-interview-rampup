class MainApp:
    def __init__(self):
        pass
    '''
    Your are given an array of positive integers nums.
    Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

    Example 1:
    Input: nums = [10, 5, 2, 6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

    ```
    TPFA

    10 5 2 6
       ^ ^ 
    product = 60 == 100
    subarray_count =  [10] [5] [10 5] [2] [5 2] [6] [5 2 6] [2 6] 
    window_start = 0
    window_end = 3
    ```
    '''

    def run(self, nums, target) -> int:
        window_start = 0
        window_end = len(nums) - 1
        if target <= 1 :
            return 0
        subarray_count = 0
        product = 1
        for window_end in range(len(nums)):
            product *= nums[window_end]
            while product >= target:
                product /= nums[window_start]
                window_start += 1
            subarray_count += window_end - window_start + 1
        return subarray_count


print(MainApp().run([10, 5, 2, 6], 100))
