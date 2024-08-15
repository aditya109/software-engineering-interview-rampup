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
		{
			name: "Example 1",
			args: args{nums: []int{2, 3, 1, 2, 4, 3}, target: 7},
			want: 2, // Subarray [4, 3] or [3, 4]
		},
		{
			name: "Example 2",
			args: args{nums: []int{1, 4, 4}, target: 4},
			want: 1, // Subarray [4]
		},
		{
			name: "Example 3",
			args: args{nums: []int{1, 1, 1, 1, 1, 1, 1, 1}, target: 11},
			want: 0, // No subarray sums to 11
		},
		{
			name: "Example 4",
			args: args{nums: []int{1, 2, 3, 4, 5}, target: 11},
			want: 3, // Subarray [3, 4, 5]
		},
		{
			name: "Example 5",
			args: args{nums: []int{1, 2, 3, 4, 5}, target: 15},
			want: 5, // Subarray [1, 2, 3, 4, 5]
		},
		{
			name: "Example 6",
			args: args{nums: []int{5, 1, 3, 5, 10, 7, 4, 9, 2, 8}, target: 15},
			want: 2, // Subarray [10, 7]
		},
		{
			name: "Single Element Success",
			args: args{nums: []int{5}, target: 5},
			want: 1, // Single element subarray
		},
		{
			name: "Single Element Failure",
			args: args{nums: []int{3}, target: 5},
			want: 0, // No subarray meets the target
		},
		{
			name: "Empty Array",
			args: args{nums: []int{}, target: 1},
			want: 0, // No subarray available
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Run(tt.args.nums, tt.args.target); got != tt.want {
				t.Errorf("Run() = %v, want %v", got, tt.want)
			}
		})
	}
}
