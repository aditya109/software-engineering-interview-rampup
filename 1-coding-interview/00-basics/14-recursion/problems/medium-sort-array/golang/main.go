package main

// func sort(arr []int, last_index int) []int{
// 	if len(arr) == 1 {
// 		return []int{arr[0]}
// 	}
// 	temp := arr[len(arr)-1]
// 	sort(arr[:len(arr)-1])
// 	insert(arr[:(len(arr)-1)], temp)
// 	return arr
// }

// func insert(arr []int, temp int) {
// 	if len(arr) == 0 || arr[len(arr)-1] <= temp {
// 		arr = append(arr, temp)
// 		return
// 	}
// 	val := arr[len(arr)-1]
// 	arr = arr[:len(arr)-1]
// 	insert(arr, temp)
// 	arr = append(arr, val)
// }

// func main() {
// 	a := []int{746, 289, 615, 548, 140, 20, 551, 586, 286, 626}
// 	fmt.Println(sort(a[:]))

// }
