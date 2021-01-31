namespace Main.Service
{
    public class MainService
    {
        /**
         * Find the max sum subarray of a fixed size K
         * Example input:
         * [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
         */
        public int FindMaxSumSubarray(int[] arr, int k)
        {
            int maxValue = int.MinValue;
            int currentRunningSum = 0;

            for (int i = 0; i < arr.Length; i++)
            {
                currentRunningSum += arr[i];
                if (i >= k - 1)
                {
                    maxValue = maxValue < currentRunningSum ? currentRunningSum : maxValue;
                    currentRunningSum -= arr[i - (k - 1)];
                }
            }
            return maxValue;
        }
    }
}
