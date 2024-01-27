package mainapp

import "testing"

func TestRun(t *testing.T) {
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Run(tt.args.nums, tt.args.target); got != tt.want {
				t.Errorf("Run() = %v, want %v", got, tt.want)
			}
		})
	}
}
