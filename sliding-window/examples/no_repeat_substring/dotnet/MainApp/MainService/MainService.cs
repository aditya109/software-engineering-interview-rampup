using System;
using System.Collections.Generic;

namespace Main.Service
{
    public class MainService
    {
        /**
         * Given a string s, find the length of the longest substring without repeating characters.
         * 
         * Example 1:
         * Input: s = "abcabcbb"
         * Output: 3
         * Explanation: The answer is "abc", with the length of 3.
         * 
         * Example 2:
         * Input: s = "bbbbb"
         * Output: 1
         * Explanation: The answer is "b", with the length of 1.
         * 
         * Example 3:
         * Input: s = "pwwkew"
         * Output: 3
         * Explanation: The answer is "wke", with the length of 3.
         * Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
         * 
         * Example 4:
         * Input: s = ""
         * Output: 0
         */

        public int Run(string s)
        {
            int windowStart = 0;
            int longestSubstringLength = int.MinValue;

            HashSet<char> uniqueCharacterSet = new HashSet<char>(); 
            for (int windowEnd = 0; windowEnd < s.Length; )
            {
                if(uniqueCharacterSet.Contains(s[windowEnd]))
                {
                    uniqueCharacterSet.Remove(s[windowStart]);
                    windowStart++;
                }
                else
                {
                    uniqueCharacterSet.Add(s[windowEnd]);
                    windowEnd++;
                    longestSubstringLength = Math.Max(longestSubstringLength, uniqueCharacterSet.Count);
                }
            }
            return s.Length == 0 ? 0 : longestSubstringLength;
        }
    }
}
