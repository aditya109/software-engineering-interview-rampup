package _01_two_sum

import (
	"reflect"
	"testing"
)

func Test_findTwoSumPairs(t *testing.T) {
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{
			name: "TC#1",
			args: args{
				nums: []int{
					8, 7, 2, 5, 3, 1,
				},
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findTwoSumPairs(tt.args.nums, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("findTwoSumPairs() = %v, want %v", got, tt.want)
			}
		})
	}
}
