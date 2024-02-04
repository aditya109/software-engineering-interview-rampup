package main

import (
	"fmt"
	"math/rand"
)

type Node struct {
	info interface{}
	prev *Node
	next *Node
}

type List struct {
	head *Node
	tail *Node
}

func (l *List) Insert(d interface{}) {
	newNode := &Node{
		info: d,
		prev: nil,
		next: nil,
	}
	if l.head == nil {
		l.head = newNode
		l.tail = newNode
	} else {
		p := l.head
		for p.next != nil {
			p = p.next
		}
		newNode.prev = p
		p.next = newNode
		l.tail = newNode
	}
}

func Show(l *List) {
	p := l.head
	for p != nil {
		fmt.Printf("-> %v ", p.info)
		p = p.next
	}
	fmt.Println()
}

func ReverseShow(l *List) {
	p := l.tail
	for p != nil {
		fmt.Printf("-> %v ", p.info)
		p = p.prev
	}
	fmt.Println()
}

func main() {
	sl := List{}
	for i := 0; i < 10; i++ {
		sl.Insert(rand.Intn(100))
	}
	Show(&sl)
	ReverseShow(&sl)
}
