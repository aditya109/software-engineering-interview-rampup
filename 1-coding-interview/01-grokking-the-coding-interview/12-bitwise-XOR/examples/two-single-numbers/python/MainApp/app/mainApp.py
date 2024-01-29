class MainApp:
    def __init__(self):
        pass

    '''
    Given an integer array nums where every element appears three times except for one, which appears exactly once. 
    Find the single element and return it.
    Example 1:
    
    Input: nums = [2,2,3,2]
    Output: 3
    '''

    '''
    Bitwise approach
    '''
    # @staticmethod
    # def run(arr):
    #     occurs_once = 0
    #     occurs_twice = 0
    #     for n in arr:
    #         occurs_once = (occurs_once ^ n) & (~occurs_twice)
    #         occurs_twice = (occurs_twice ^ n) & (~occurs_once)
    #     return occurs_once

    '''
    Hashmap approach
    '''
    @staticmethod
    def run(arr):
        n_map = dict()
        for n in arr:
            if n in n_map:
                n_map[n] += 1
            else:
                n_map[n] = 1
        for k, v in n_map.items():
            if v == 1:
                return k
        return None

