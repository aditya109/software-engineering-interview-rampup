package main

type Node struct {
	info interface{}
	next *Node
}

type List struct {
	head *Node
}

func (l *List) Insert(info interface{}) {
	newNode := &Node{
		info: info,
		next: nil,
	}

	if l.head == nil {
		l.head = newNode
		newNode.next = l.head
	} else {
		p := l.head
		for {
			if p.next == l.head {
				// reached 
			}
			p = p.next
		}
		p.next = newNode

	}
}

func main() {

}
