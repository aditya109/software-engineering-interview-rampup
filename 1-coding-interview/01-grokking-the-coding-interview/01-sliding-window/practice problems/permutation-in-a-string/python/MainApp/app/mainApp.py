from collections import Counter
import copy


class MainApp:
    def __init__(self):
        pass
    '''
    Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

    Example 1:
    Input: s1 = "ab" s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").
    '''

    def run(self, s1, s2):
        s1_count = dict(Counter(s1))
        window_start = 0
        window_count = dict()
        if s1 == "":
            return True
        if s2 == "":
            return False
        for window_end in range(len(s2)):
            if s2[window_end] not in set(window_count.keys()):
                window_count[s2[window_end]] = 1
            elif s2[window_end] in set(window_count.keys()):
                window_count[s2[window_end]] += 1
            if window_end >= len(s1):
                if window_count[s2[window_start]] == 1:
                    del window_count[s2[window_start]]
                else:
                    window_count[s2[window_start]] -= 1
                window_start += 1
            if window_count == s1_count:
                return True
        return False

