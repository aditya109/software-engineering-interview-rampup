package io.github.mainapp;

public class MainApp {
    /**
    * Find the max sum of subarray of a fixed size 3
    * Example input:
    * [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    * === 16
    */
    public int Run(int [] arr, int k) {
        int maxValue = Integer.MIN_VALUE;
        int currentRunningSum = 0;

        for (int i = 0; i < arr.length; i++)
        {
            currentRunningSum += arr[i];
            if (i >= k - 1)
            {
                maxValue = Math.max(maxValue, currentRunningSum);
                currentRunningSum -= arr[i - (k - 1)];
            }
        }
        return maxValue;
    }
}
