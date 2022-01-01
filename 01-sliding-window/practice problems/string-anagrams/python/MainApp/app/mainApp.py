from collections import Counter


class MainApp:
    def __init__(self):
        pass
    '''
    Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

    Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

    The order of output does not matter.

    Example 1:

    Input:
    s: "cbaebabacd" p: "abc"

    Output:
    [0, 6]

    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
    Example 2:

    Input:
    s: "abab" p: "ab"

    Output:
    [0, 1, 2]

    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
    '''

    def run(self, s, p):
        p_counter = dict(Counter(p))
        s_length = len(s)
        p_length = len(p)
        window_start = 0
        anagrams_start_indices = []

        window_counter = dict()
        for window_end in range(s_length):
            if s[window_end] not in set(window_counter):
                window_counter[s[window_end]] = 1
            else:
                window_counter[s[window_end]] += 1
            if p_counter == window_counter:
                anagrams_start_indices.append(window_start)
            if window_end >= p_length - 1:
                if window_counter[s[window_start]] == 1:
                    del window_counter[s[window_start]]
                else:
                    window_counter[s[window_start]] -= 1
                window_start += 1
        return anagrams_start_indices
