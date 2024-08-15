package mainapp

import "math"

type Node struct {
	Left  *Node
	Right *Node
	Value int
}

func getHeight(n *Node) int {
	if n == nil {
		return 0
	}
	return 1 + int(math.Max(float64(getHeight(n.Left)), float64(getHeight(n.Right))))
}
