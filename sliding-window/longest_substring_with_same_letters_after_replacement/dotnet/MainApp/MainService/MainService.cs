

using System;

namespace Main.Service
{
    public class MainService
    {
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
        public int Run(string s, int k)
        {
            int length = s.Length;              // length stores the string `s` length
            int[] char_counts = new int[26];    // char_counts stores the frequency according to all 26 letters of alphabets

            int window_start = 0;               // window_start denotes the left end of the window
            int max_length = 0;                 // max_length stores the longest repeating substring length found so far
            int max_count = 0;                  // max_count stores the longest repeating substring length of the window

            // iterating the rear of the window towards the end of the string
            for (int window_end = 0; window_end < length; window_end++)
            {
                // for each letter of the window, 
                // we find the corresponding alphabetical index in the character and increase its frequency by 1 
                char_counts[s[window_end] - 'A']++;
                // we store the frequency of the character at rear of the window in a temp variable
                int current_char_count = char_counts[s[window_end] - 'A'];
                // then we store the maximum of all the frequencies of the characters in the sliding window in the max_count
                max_count = Math.Max(max_count, current_char_count);
                
                // <window_end - window_start - max_count + 1> is count of unique characters within the window
                // iterating to shorten the window
                while(window_start <= window_end && window_end - window_start - max_count + 1 > k)
                {
                    char_counts[s[window_start] - 'A']--;
                    window_start++;
                }
                max_length = Math.Max(max_length, window_end - window_start + 1);
            }
            return max_length;
        }
    }
}
