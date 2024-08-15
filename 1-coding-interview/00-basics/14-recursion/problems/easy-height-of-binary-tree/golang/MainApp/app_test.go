package mainapp

import (
	"testing"
)

func Test_getHeight(t *testing.T) {
	type args struct {
		n *Node
	}

	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "TC #1",
			args: args{
				n: &Node{
					Value: 1,
					Left: &Node{
						Value: 2,
						Left:  &Node{Value: 4},
					},
					Right: &Node{
						Value: 3,
						Right: &Node{Value: 5},
					},
				},
			},
			want: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getHeight(tt.args.n); got != tt.want {
				t.Errorf("getHeight() = %v, want %v", got, tt.want)
			}
		})
	}
}
