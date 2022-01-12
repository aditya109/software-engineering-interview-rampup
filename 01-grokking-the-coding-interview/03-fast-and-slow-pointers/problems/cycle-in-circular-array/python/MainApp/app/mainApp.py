class MainApp:
    def __init__(self):
        pass

    '''
    You are playing a game involving a circular array of non-zero integers nums. 
    Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

    If nums[i] is positive, move nums[i] steps forward, and
    If nums[i] is negative, move nums[i] steps backward.
    Since the array is circular, you may assume that moving forward from the last element puts you on the first element, 
    and moving backwards from the first element puts you on the last element.
    
    A cycle in the array consists of a sequence of indices seq of length k where:
    
    Following the movement rules above results in the repeating index sequence:
    seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
    Every nums[seq[j]] is either all positive or all negative.
    k > 1
    Return true if there is a cycle in nums, or false otherwise.
    
    Example 1:
    Input: nums = [2,-1,1,2,2]
    Output: true
    Explanation:
    There is a cycle from index 0 -> 2 -> 3 -> 0 -> ...
    The cycle's length is 3.

    === === === === === === === === === === === === === === === === === === === === === === === === ===

    Example 2:
    Input: nums = [-1,2]
    Output: false
    Explanation:
    The sequence from index 1 -> 1 -> 1 -> ... is not a cycle because the sequence's length is 1.
    By definition the sequence's length must be strictly greater than 1 to be a cycle.

    === === === === === === === === === === === === === === === === === === === === === === === === ===

    Example 3:
    Input: nums = [-2,1,-1,-2,-2]
    Output: false
    Explanation:
    The sequence from index 1 -> 2 -> 1 -> ... is not a cycle because nums[1] is positive, but nums[2] is negative.
    Every nums[seq[j]] must be either all positive or all negative.
    
    === === === === === === === === === === === === === === === === === === === === === === === === === 
    '''

    @staticmethod
    def run(arr: list) -> bool:
        slow = fast = 0



        """
        === -> 2 -> -1 -> 1 -> 2 -> 2 -> ===
              s^
              f^
              5 - 0 - 3 = 2
              
        def change_fast(chip, state):
            if state == "positive":
                return (fast + arr[chip]) % (len(arr))
            else:
                if (fast - arr[chip]) <= 0:
                    return len(arr) - fast - arr[chip]
                return fast - arr[chip]
        
        def check_fast(x, state):
            if state == "positive":
                if arr[x] > 0:
                    return True
                else:
                    return False
            else:
                if arr[x] < 0:
                    return True
                else:
                    return False
        has_cycle = False
        for index, element in enumerate(arr):
            counter = 0         # for counting number of loop links
            if element >= 0:
                # assigning sign
                sign = "positive"
            else:
                sign = "negative"
            # putting fast at slow
            fast = slow
            prev_fast = fast
            while True:
                if check_fast(fast, sign):
                    fast = change_fast(fast, sign)
                    counter += 1
                    if slow < fast < prev_fast:
                        # fast has rotated past slow
                        has_cycle = False
                        break
                    else:
                        prev_fast = fast
                else:
                    break
                if fast == slow:
                    has_cycle = True
                    return has_cycle

            if not has_cycle and counter <= 1:
                has_cycle = False
            else:
                slow += 1
        return has_cycle

        """



print(MainApp().run([1, 2]))





















