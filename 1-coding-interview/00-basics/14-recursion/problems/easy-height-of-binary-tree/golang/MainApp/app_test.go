package mainapp

import "testing"

func TestRun(t *testing.T) {
	type args struct {
		t *BinaryTree
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Run(tt.args.t); got != tt.want {
				t.Errorf("Run() = %v, want %v", got, tt.want)
			}
		})
	}
}
