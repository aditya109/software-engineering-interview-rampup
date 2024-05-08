package main

import "fmt"

type Stack [] int

func (s *Stack) Push(v int) {
	*s = append(*s, v)
}

func (s *Stack) Pop() int {
	if s.IsEmpty() {
		return -1
	} else {
		top := (*s)[len(*s)-1]
		*s = (*s)[:len(*s)-1]
		return top
	}
}

func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

func main() {
	st := Stack{}
	st.Push(1)
	st.Push(2)
	st.Push(3)
	fmt.Println(st.Pop())
	fmt.Println(st.Pop())
	fmt.Println(st.Pop())
	fmt.Println(st.Pop())
}