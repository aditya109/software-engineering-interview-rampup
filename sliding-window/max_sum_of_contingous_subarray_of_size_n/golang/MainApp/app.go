package mainapp

import "math"

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
