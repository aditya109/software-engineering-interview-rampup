package main

import (
	"container/heap"
	"fmt"
)

type Item struct {
	priority int
	index    int
	value    interface{}
}

type PQ []*Item

func (pq PQ) Len() int { return len(pq) }

func (pq PQ) Less(i, j int) bool {
	return pq[i].priority > pq[j].priority
}

func (pq PQ) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PQ) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PQ) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	item.index = -1
	*pq = old[:n-1]
	return item
}

func (pq *PQ) update(item *Item, value interface{}, priority int) {
	item.value = value
	item.priority = priority
	heap.Fix(pq, item.index)
}

func main() {
	items := map[string]int{
		"banana": 3,
		"apple":  2,
		"pear":   1,
	}
	i := 0
	pq := make(PQ, len(items))
	for v, p := range items {
		pq[i] = &Item{
			priority: p,
			index:    i,
			value:    v,
		}
		i++
	}
	heap.Init(&pq)

	item := &Item{
		priority: 5,
		value:    "orange",
	}
	heap.Push(&pq, item)
	pq.update(item, item.value, item.priority)

	for pq.Len() > 0 {
		item := heap.Pop(&pq).(*Item)
		fmt.Println(item.value, item.priority)
	}
}
