/*
Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.

Examples:

Input:
arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
Output: 3 4 5 6 7 1 2

Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
Output: 5 6 7 1 2 3 4

*/

package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func RotateArrayByDTimes(N int, arr []int, d int) []int {
	if d > 0 {
		// left rotate the array
		return append(arr[d:], arr[:d]...)
	} else {
		//  right rotate the array
		return append(arr[len(arr)+d:], arr[:len(arr)+d]...)
	}
}

func checkError(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	data, err := os.ReadFile("./input.txt")
	checkError(err)
	dataInString := string(data)
	parameters := strings.Split(dataInString, "\n")
	N, err := strconv.Atoi(parameters[0])
	checkError(err)
	var arr []int
	arrInString := strings.Split(parameters[1], " ")
	for _, v := range arrInString {
		vOfNumberType, err := strconv.Atoi(v)
		checkError(err)
		arr = append(arr, vOfNumberType)
	}
	d, err := strconv.Atoi(parameters[2])
	checkError(err)
	fmt.Println("result = ", RotateArrayByDTimes(N, arr, d))
}
