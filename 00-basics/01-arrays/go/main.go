package main

import "fmt"

func main() {
	var a [2]string
	a[0] = "hello"
	a[1] = "world"

	primes := [6]int{2,3,4,5}
	// [2 3 4 5 0 0]
	fmt.Println(primes)

	// taking array as an input 
	fmt.Println("enter the size of list to be created:")
	var n int
	fmt.Scanln(&n)

	for i := 0; i < n; i ++ {
		fmt.Scan(&a[i])
	}
	
	// slices 
	var subsetOfPrimesAsSlice []int = primes[1:4]
	fmt.Println(subsetOfPrimesAsSlice)
	subsetOfPrimesAsSlice[2] = 45
	fmt.Println(subsetOfPrimesAsSlice)

	// slice literals - DO NOT TREAT AS CONSTANTS, rather treat them as dynamic and tools to create slices of varying lengths.
	var anotherPrimesAsSliceLiterals = []int{1,2,3,4,5}
	// we can create new slices from this 
	newSlice := anotherPrimesAsSliceLiterals[1:3]
	fmt.Println(newSlice)
	
	k := get()
	fmt.Println(k)
	set(k)
	fmt.Println(k)
	// OMG wait, for years I thought I was creating arrays while coding, damn I suck :( !!!!!

}

func get() []int {
	var a = []int{1, 2, 3, 4}
	return a
}

func set(a []int) {
	a[3] = 435
} 

