# Mediator Pattern

## What is it ?

It lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.

### Basic Structure

<image src="https://github.com/aditya109/software-engineering-interview-rampup/blob/main/2-system-design-and-rest/2-design-patterns/assets/mediator-pattern.png?raw=true"/>


### Example

```go
package main

import "fmt"

type Mediator interface {
	canArrive(Train) bool
	notifyAboutDeparture()
}

type Train interface {
	arrive()
	depart()
	permitArrival()
}

type PassengerTrain struct {
	mediator Mediator
}

func (pt *PassengerTrain) arrive() {
	if !pt.mediator.canArrive(pt) {
		fmt.Println("PassengerTrain: Arrival blocked, waiting")
		return
	}
	fmt.Println("PassengerTrain: Arrived")
}

func (pt *PassengerTrain) depart() {
	fmt.Println("PassengerTrain: Leaving")
	pt.mediator.notifyAboutDeparture()
}

func (pt *PassengerTrain) permitArrival() {
	fmt.Println("PassengerTrain: Arrival Permitted, arriving")
	pt.arrive()
}

type FreightTrain struct {
	mediator Mediator
}

func (pt *FreightTrain) arrive() {
	if !pt.mediator.canArrive(pt) {
		fmt.Println("FreightTrain: Arrival blocked, waiting")
		return
	}
	fmt.Println("FreightTrain: Arrived")
}

func (pt *FreightTrain) depart() {
	fmt.Println("FreightTrain: Leaving")
	pt.mediator.notifyAboutDeparture()
}

func (pt *FreightTrain) permitArrival() {
	fmt.Println("FreightTrain: Arrival Permitted, arriving")
	pt.arrive()
}

type StationManager struct {
	isPlatformFree bool
	trainQueue     []Train
}

func newStationManager() *StationManager {
	return &StationManager{
		isPlatformFree: true,
	}
}

func (sm *StationManager) canArrive(train Train) bool {
	if sm.isPlatformFree {
		sm.isPlatformFree = false
		return true
	}
	sm.trainQueue = append(sm.trainQueue, train)
	return false
}

func (sm *StationManager) notifyAboutDeparture() {
	if !sm.isPlatformFree {
		sm.isPlatformFree = true
	}
	if len(sm.trainQueue) > 0 {
		firstTrainInQueue := sm.trainQueue[0]
		sm.trainQueue = sm.trainQueue[1:]
		firstTrainInQueue.permitArrival()
	}
}

func main() {
	stationManager := newStationManager()

	passengerTrain := PassengerTrain{
		mediator: stationManager,
	}

	freightTrain := FreightTrain{
		mediator: stationManager,
	}

	passengerTrain.arrive()
	freightTrain.arrive()
	passengerTrain.depart()
}


```

## Where to apply ?

- When it’s hard to change some of the classes because they are tightly coupled to a bunch of other classes.
- When you can’t reuse a component in a different program because it’s too dependent on other components.
- When you find yourself creating tons of component subclasses just to reuse some basic behavior in various contexts.

### Pros

- Single Responsibility Principle. You can extract the communications between various components into a single place, making it easier to comprehend and maintain.
- Open/Closed Principle. You can introduce new mediators without having to change the actual components.
- You can reduce coupling between various components of a program.
- You can reuse individual components more easily.

### Cons

- Over time a mediator can evolve into a God Object.

