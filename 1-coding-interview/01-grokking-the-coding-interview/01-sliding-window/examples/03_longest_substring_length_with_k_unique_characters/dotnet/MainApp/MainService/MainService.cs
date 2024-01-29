using System;
using System.Collections.Generic;
using System.Linq;

namespace Main.Service
{
    public class MainService
    {
        /**
         * Find the longest substring length with atmost 2 distinct characters
         * Example input:
         * ['A', 'A', 'A', 'H', 'H', 'I', 'B', 'C']
         * === 5
         */
        public int LongestSubstringLength(char[] arr, int k)
        {
            int windowStart = 0;
            int longestSubstringLength = int.MinValue;
            int currentSubstringLength = 0;
            Dictionary<char, int> hashFreqTable = new Dictionary<char, int>();

            for (int windowEnd = 0; windowEnd < arr.Length; windowEnd++)
            {
                currentSubstringLength++;

                if(hashFreqTable.ContainsKey(arr[windowEnd]))
                {
                    hashFreqTable[arr[windowEnd]] += 1;
                }
                else
                {
                    hashFreqTable[arr[windowEnd]] = 1;
                }

                List<char> keys = new List<char>(hashFreqTable.Keys);
                if(keys.Count() > k)
                {
                    longestSubstringLength = Math.Max(longestSubstringLength, currentSubstringLength - 1);
                    hashFreqTable[arr[windowStart]] -= 1;
                    currentSubstringLength--;
                    windowStart++;
                }
            }
            return longestSubstringLength;
        }
    }
}
