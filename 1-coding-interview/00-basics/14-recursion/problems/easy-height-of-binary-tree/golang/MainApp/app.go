package mainapp

type BinaryNode struct {
	left  *BinaryNode
	right *BinaryNode
	data  int64
}

type BinaryTree struct {
	root *BinaryNode
}

func (t *BinaryTree) insert(data int64) *BinaryTree {
	if t.root == nil {
		t.root = &BinaryNode{
			data:  data,
			left:  nil,
			right: nil,
		}
	} else {
		t.root.insert(data)
	}
	return t
}

func (n *BinaryNode) insert(data int64) {
	if n == nil {
		return
	} else if data <= n.data {
		if n.left == nil {
			n.left = &BinaryNode{
				data:  data,
				left:  nil,
				right: nil,
			}
		} else {
			n.left.insert(data)
		}
	} else {
		if n.right == nil {
			n.right = &BinaryNode{
				data:  data,
				left:  nil,
				right: nil,
			}
		} else {
			n.right.insert(data)
		}
	}
}

func Run(t *BinaryTree) int {
	return 0
}
