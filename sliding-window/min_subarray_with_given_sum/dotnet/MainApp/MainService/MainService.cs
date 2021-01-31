using System;

namespace Main.Service
{
    public class MainService
    {
        /**
        * Find the min subarray length with sum <= 8
        * Example input:
        * [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
        * === 1
        */
        public int SmallestSubarray(int targetSum, int[] arr)
        {
            int minWindowSize = int.MaxValue;
            int currentWindowSum = 0;
            int windowStart = 0;
            for (int windowEnd = 0; windowEnd < arr.Length; windowEnd++)
            {
                currentWindowSum += arr[windowEnd];

                while (currentWindowSum >= targetSum)
                {
                    minWindowSize =
                        Math.Min(minWindowSize, (windowEnd - windowStart + 1));
                    currentWindowSum -= arr[windowStart];
                    windowStart++;
                }
            }
            return minWindowSize;
        }
    }
}
