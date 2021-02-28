from collections import Counter
import collections


class MainApp:
    def __init__(self):
        pass
    '''
    /**
    * Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. 
    * Find the length of a longest substring containing all repeating letters you can get after performing the above operations.
    * 
    * Example 1:
    * Input: s = "ABAB", k = 2
    * Output: 4
    * Explanation: Replace the two 'A's with two 'B's or vice versa.
    * 
    * Example 2:
    * Input: s = "AABABBA", k = 1
    * Output: 4
    * Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA". 
    * The substring "BBBB" has the longest repeating letters, which is 4.
    * 
    */
    '''

    # def run(self, s, k):
    #     s = s.upper()
    #     length = len(s)
    #     char_counts = [0] * 26

    #     window_start = 0
    #     maximum_length = 0
    #     maximum_count = 0

    #     for window_end in range(length):
    #         char_counts[ord(s[window_end]) - ord('A')] += 1
    #         current_char_count = char_counts[ord(s[window_end]) - ord('A')]
    #         maximum_count = max(maximum_count, current_char_count)

    #         while window_start <= window_end and window_end - window_start - maximum_count + 1 > k:
    #             char_counts[ord(s[window_start]) - ord('A')] -= 1
    #             window_start += 1
    #         maximum_length = max(maximum_length, window_end - window_start + 1)
    #     return maximum_length

    def run(self, s, k):
        s = s.upper()
        maximum_count = window_start = 0
        char_counts = collections.Counter()

        for window_end in range(len(s)):
            char_counts[s[window_end]] += 1
            maximum_count = max(maximum_count, char_counts[s[window_end]])
            if window_end - window_start + 1 > maximum_count + k:
                char_counts[s[window_start]] -= 1
                window_start += 1
        return len(s) - window_start
