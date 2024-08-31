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
