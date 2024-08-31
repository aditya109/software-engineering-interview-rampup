package main

import "fmt"

type Observer interface {
	update(string)
	getId() string
}

type Subject interface {
	register(o Observer)
	deregister(o Observer)
	notifyAll()
}

type Item struct {
	observerList []Observer
	name         string
	inStock      bool
}

func newItem(name string) *Item {
	return &Item{
		name: name,
	}
}

func (item *Item) register(o Observer) {
	item.observerList = append(item.observerList, o)
}

func (item *Item) deregister(o Observer) {
	item.observerList = removeFromSlice(item.observerList, o)
}

func (item *Item) updateAvailability() {
	fmt.Println("Item is not in stock\n", item.name)
	item.inStock = true
	item.notifyAll()
}

func (item *Item) notifyAll() {
	for _, o := range item.observerList {
		o.update(item.name)
	}
}

func removeFromSlice(observerList []Observer, observerToRemove Observer) []Observer {
	observerListLength := len(observerList)
	for idx, observer := range observerList {
		if observerToRemove.getId() == observer.getId() {
			observerList[observerListLength-1], observerList[idx] = observerList[idx], observerList[observerListLength-1]
			return observerList[:observerListLength-1]
		}
	}
	return observerList
}

type Customer struct {
	id string
}

func (c *Customer) update(itemName string) {
	fmt.Printf("Sending email to customer %s for item %s\n", c.id, itemName)
}

func (c *Customer) getId() string {
	return c.id
}

func main() {
	shirtItem := newItem("Nike Shirt")

	observerFirst := &Customer{id: "abc@gmail.com"}
	observerSecond := &Customer{id: "xyz@gmail.com"}

	shirtItem.register(observerFirst)
	shirtItem.register(observerSecond)

	shirtItem.updateAvailability()
}
