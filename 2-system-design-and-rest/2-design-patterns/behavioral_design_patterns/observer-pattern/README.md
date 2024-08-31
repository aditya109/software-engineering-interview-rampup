# Observer Pattern

## What is it ?

It lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

### Basic Structure

<image src="https://github.com/aditya109/software-engineering-interview-rampup/blob/main/2-system-design-and-rest/2-design-patterns/assets/observer-pattern.png?raw=true"/>

### Example

```go
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

```

## Where to apply ?

- When changes to the state of one object may require changing other objects, and the actual set of objects is unknown beforehand or changes dynamically.
- When some objects in your app must observe others, but only for a limited time or in specific cases.

### Pros

- Open/Closed Principle. You can introduce new subscriber classes without having to change the publisher’s code (and vice versa if there’s a publisher interface). 
- You can establish relations between objects at runtime.

### Cons
- 
- Subscribers are notified in random order.
