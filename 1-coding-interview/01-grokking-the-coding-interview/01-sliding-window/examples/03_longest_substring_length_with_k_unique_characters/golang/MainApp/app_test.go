package mainapp

import "testing"

func TestRun(t *testing.T) {
	type args struct {
		input string
		k     int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Case 1: k = 2",
			args: args{
				input: "AAAHHIBC",
				k:     2,
			},
			want: 5, // "AAAHH" or "HHIB"
		},
		{
			name: "Case 2: k = 3",
			args: args{
				input: "AAAHHIBC",
				k:     3,
			},
			want: 6, // "AAAHHI" or "HHIBC"
		},
		{
			name: "Case 3: k = 1",
			args: args{
				input: "AAAHHIBC",
				k:     1,
			},
			want: 3, // "AAA" or "HH"
		},
		{
			name: "Case 4: Single character repeated",
			args: args{
				input: "AAAA",
				k:     2,
			},
			want: 4, // "AAAA"
		},
		{
			name: "Case 5: Distinct characters",
			args: args{
				input: "ABCD",
				k:     2,
			},
			want: 2, // "AB", "BC", or "CD"
		},
		{
			name: "Case 6: Empty input",
			args: args{
				input: "",
				k:     2,
			},
			want: 0, // No substring
		},
		{
			name: "Case 7: k = 0",
			args: args{
				input: "AABC",
				k:     0,
			},
			want: 0, // No valid substring
		},
		{
			name: "Case 8: k greater than number of distinct characters",
			args: args{
				input: "ABC",
				k:     5,
			},
			want: 3, // "ABC"
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Run(tt.args.input, tt.args.k); got != tt.want {
				t.Errorf("Run() = %v, want %v", got, tt.want)
			}
		})
	}
}
