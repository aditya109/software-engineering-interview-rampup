package mainapp

import "testing"

func TestRun(t *testing.T) {
	arguments := []struct {
		arr []int
		k int
		expectedResult int
	} {
		{[]int{ 4, 2, 1, 7, 8, 1, 2, 8, 1, 0 }, 3, 16},
		{[]int{ 4, 2, 1, 7, 8, 1, 2, 8, 1, 0 }, 4, 19},
		{[]int{ 4, 2, 1, 7, 8, 1, 2, 8, 1, 0 }, 5, 26},
		{[]int{ 4, 2, 1, 7, 8, 8, 1, 0 }, 3, 23},
	}

	for _, argument := range arguments {
		actualResult := Run(argument.arr, argument.k)
		if actualResult != argument.expectedResult {
			t.Errorf("Incorrect answer, got: %d expected: %d.", actualResult, argument.expectedResult)
		}
	}
}
