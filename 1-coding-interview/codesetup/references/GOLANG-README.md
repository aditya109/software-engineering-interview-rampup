# Steps to run example codebase in <img src="https://cdn.svgporn.com/logos/gopher.svg" height="50"/> 

> The Golang implementation of a particular problem is written such that the code can be freely tested amongst numerous test cases.

To run a particular code implementation in `golang` for a particular problem set, navigate to the specific problem set.  

Let's say the problem set is `max_sum_of_contingous_subarray_of_size_n` under `sliding-window`.

So we navigate to `grokking-the-coding-interview` > `sliding-window` > `max_sum_of_contingous_subarray_of_size_n` > `golang` > `MainApp`.

For `golang`, you could either use any text editor of your choice. I am using `VS Code` for demonstration.

## Repository Explanation

1. The directory structure visible would be something like this:

   ```powershell
   MAINAPP
   ├───app.go
   └───app_test.go
   ```

2. `app.go` is the program where actual code resides. The main code resides within `Run()`.

   ```c#
   package mainapp
   
   func Run(x int, y int) int {
   	return 0
   }
   ```

3. `app_test.go` is the program where unit tests reside.

   ```c#
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
   
   ```

## Steps for `VS Code` users:

1. Open the `MainApp` in `VS Code`.

2. Open `Powershell Terminal`.

   ```powershell
   🐳 :: MainApp » go test
   PASS
   ok      github.com/aditya109/grokking-the-coding-interview/codesetup/golang/MainApp   0.163s
   ```

