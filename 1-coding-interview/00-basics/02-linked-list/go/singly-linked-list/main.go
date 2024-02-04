package main

import (
	"fmt"
	"math/rand"
)

type Node struct {
	info interface{}
	next *Node
}

type List struct {
	head *Node
}

func (l *List) Insert(d interface{}) {
	newNode := &Node{
		info: d,
		next: nil,
	}

	if l.head == nil {
		l.head = newNode
	} else {
		p := l.head
		for p.next != nil {
			p = p.next
		}
		p.next = newNode
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

func main() {
	sl := List{}
	for i := 0; i < 5; i++ {
		sl.Insert(rand.Intn(100))
	}
	Show(&sl)
}
