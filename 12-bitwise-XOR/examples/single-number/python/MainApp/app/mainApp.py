class MainApp:
    def __init__(self):
        pass

    '''
    Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.
    Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
    
    Example 1:
    
    Input: nums = [2,2,1]
                   ^
    Output: 1

    '''

    @staticmethod
    def run(arr):
        xor = 0
        for n in arr:
            xor ^= n
        return xor
