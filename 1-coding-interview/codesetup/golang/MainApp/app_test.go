package mainapp

import "testing"

func TestRun(t *testing.T) {
	arguments := []struct {
		x int
		y int
		n int
	} {
		{1, 1, 2},
		{1, 2, 3},
		{2, 2, 4},
		{5, 2, 7},
	}

	for _, argument := range arguments {
		actualResult := Run(argument.x, argument.y)
		if actualResult != 0 {
			t.Errorf("Incorrect answer, got: %d expected: %d.", actualResult,0)
		}
	}
}
