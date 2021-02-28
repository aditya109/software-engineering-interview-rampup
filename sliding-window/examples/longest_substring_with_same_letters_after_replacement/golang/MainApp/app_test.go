package mainapp

import "testing"

func TestRun(t *testing.T) {
	arguments := []struct {
		s      string
		k      int
		expectedResult int
	}{
		{"ABAB", 2, 4},
		{"AABAABA", 1, 4},
	}

	for _, argument := range arguments {
		actualResult := Run(argument.s, argument.k)
		if actualResult != argument.expectedResult {
			t.Errorf("Incorrect answer, got: %d expected: %d.", actualResult, argument.expectedResult)
		}
	}
}
