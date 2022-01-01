package main
import "math"

/**
* Find the max sum of subarray of a fixed size 3
* Example input:
* [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
* === 16
 */

// Run function
func Run(arr []int, k int) int {
	maxValue := -1
	currentRunningSum := 0

	for i := 0; i < len(arr) ; i++{
		currentRunningSum += arr[i]
		if i >= k - 1 {
			maxValue = int(math.Max(float64(currentRunningSum), float64(maxValue)))
			currentRunningSum -= arr[i - (k - 1)]
		}
	}
	return maxValue
}
