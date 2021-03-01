from collections import Counter


class MainApp:
    def __init__(self):
        pass
    '''
    Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

    Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

    Example 1:

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Example 2:

    Input: s = "a", t = "a"
    Output: "a"
    '''

    def run(self, s, t):
        s_length = len(s)
        t_length = len(t)

        window_start = 0

        resultant_string = ""
        resultant_string_length = float('inf')

        t_counter = dict(Counter(t))
        window_counter = dict()

        # shifting window_end if we do not have all the characters in t_counter
        # shifting window_start if we have all the character in t_counter
        for window_end in range(s_length):
            if s[window_end] in set(t_counter):
                if s[window_end] not in set(window_counter):
                    window_counter[s[window_end]] = 1
                elif s[window_end] in set(window_counter):
                    window_counter[s[window_end]] += 1
            while window_counter == t_counter:
                if resultant_string_length > window_end - window_start + 1:
                    resultant_string = s[window_start:window_end+1]
                    resultant_string_length = min(resultant_string_length, window_end - window_start + 1)
                if window_counter[s[window_start]] == 1:
                    del window_counter[s[window_start]]
                else:
                    window_counter[s[window_start]] -= 1
                window_start += 1
