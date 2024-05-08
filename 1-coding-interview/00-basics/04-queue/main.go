package main

import "fmt"

type Q []int

func (q *Q) enqueue(v int) {
	*q = append(*q, v)
}

func (q *Q) dequeue() int {
	if q.IsEmpty() {
		return -1
	}
	first := (*q)[0]
	if len(*q) == 1 {
		*q = Q{}
	} else {
		*q = (*q)[1:]
	}
	return first
}

func (q *Q) IsEmpty() bool {
	return len(*q) == 0
}

func main() {
	var queue = &Q{} // Make a queue of ints.

	queue.enqueue(10)

	fmt.Println("Queue:", *queue)
	
	fmt.Println("Dequeued element: ", queue.dequeue())
	fmt.Println("Queue:", *queue)
	fmt.Println("Dequeued element: ", queue.dequeue())
	fmt.Println("Queue:", *queue)

}
