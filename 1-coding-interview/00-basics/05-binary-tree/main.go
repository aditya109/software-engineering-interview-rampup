package main

import (
	"fmt"
	"math"
)

type BinaryNode struct {
	left  *BinaryNode
	right *BinaryNode
	data  int64
}

type BinaryTree struct {
	root *BinaryNode
}

func (t *BinaryTree) insert(data int64) {
	if t.root == nil {
		t.root = &BinaryNode{
			left: nil, right: nil, data: data,
		}
	} else {
		t.root.insert(data)
	}
}

func (n *BinaryNode) insert(data int64) {
	if n == nil {
		return
	} else if data <= n.data {
		if n.left == nil {
			n.left = &BinaryNode{
				left: nil, right: nil, data: data,
			}
		} else {
			n.left.insert(data)
		}
	} else {
		if n.right == nil {
			n.right = &BinaryNode{
				left: nil, right: nil, data: data,
			}
		} else {
			n.right.insert(data)
		}
	}
}

func inorder(root *BinaryNode) {
	if root != nil {
		inorder(root.left)
		fmt.Printf("%d ", root.data)
		inorder(root.right)
	}
}

func checkIfTreeIsBinarySearchType(tree *BinaryTree) bool {
	if root := tree.root; root == nil {
		return true
	} else {
		return checkIfNodeIsBinarySearchType(root, math.MinInt64, math.MaxInt64)
	}
}

func checkIfNodeIsBinarySearchType(root *BinaryNode, min int64, max int64) bool {
	if root == nil {
		return true
	}
	if root.data <= min || root.data >= max {
		return false
	}
	return checkIfNodeIsBinarySearchType(root.left, min, max) && checkIfNodeIsBinarySearchType(root.right, min, max)
}

func IsBalanced(tree *BinaryTree) bool {
	return DFSHeight(tree.root) != -1
}

func DFSHeight(root *BinaryNode) int {
	if root == nil {
		return 0
	}
	left_height := DFSHeight(root.left)
	if left_height == -1 {
		return -1
	}
	right_height := DFSHeight(root.right)
	if right_height == -1 {
		return -1
	}

	if math.Abs(float64(left_height)-float64(right_height)) > 1 {
		return -1
	}
	return max(left_height, right_height) + 1

}

func main() {
	tree := &BinaryTree{}
	tree.insert(17)
	tree.insert(19)
	tree.insert(11)
	tree.insert(14)
	tree.insert(9)
	inorder(tree.root)
	// fmt.Println(checkIfTreeIsBinarySearchType(tree))
	fmt.Println(IsBalanced(tree))
}
