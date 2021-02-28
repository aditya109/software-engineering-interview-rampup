import sys


class MainApp:
    def __init__(self):
        pass
    '''
    Given a string S, find the length of the longest substring T that contains at most k distinct characters.

    Example 1:

    Input: S = "eceba" and k = 3
    Output: 4
    Explanation: T = "eceb"

    Example 2:

    Input: S = "WORLD" and k = 4
    Output: 4
    Explanation: T = "WORL" or "ORLD"
    '''

    def run(self, s, k):
        window_start = 0
        longest_substring_length = float('-inf')
        current_substring_length = 0

        hash_frequency_table = dict()

        for window_end in range(len(s)):
            current_substring_length += 1
            unique_keys = hash_frequency_table.keys()

            if s[window_end] in unique_keys:
                hash_frequency_table[s[window_end]] += 1
            else:
                hash_frequency_table[s[window_end]] = 1

            if len(unique_keys) > k:
                longest_substring_length = max(
                    longest_substring_length, current_substring_length - 1)
                hash_frequency_table[s[window_start]] -= 1
                current_substring_length -= 1
                window_start += 1
        return longest_substring_length
