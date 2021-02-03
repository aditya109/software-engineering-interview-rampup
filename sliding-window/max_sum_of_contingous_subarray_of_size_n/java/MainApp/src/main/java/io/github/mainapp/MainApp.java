package io.github.mainapp;

public class MainApp {
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
