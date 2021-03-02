import sys


class MainApp:
    def __init__(self):
        pass
    '''
    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    Example 4:

    Input: s = ""
    Output: 0
    '''

    def run(self, s: str) -> int:
        window_start = 0
        longest_substring_length = float('-inf')

        unique_character_set = set()
        for window_end in range(len(s)):
            if s[window_end] in unique_character_set:
                unique_character_set.discard(s[window_start])
                window_start += 1
            else:
                unique_character_set.add(s[window_end])
                window_end += 1
            longest_substring_length = max(
                longest_substring_length, len(unique_character_set))
        return (longest_substring_length, 0)[len(s) == 0]
