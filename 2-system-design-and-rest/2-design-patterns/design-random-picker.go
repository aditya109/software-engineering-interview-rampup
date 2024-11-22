package main

import (
	"fmt"
	"math/rand"
	"time"
)

// DesignPatterns is a list of some common design patterns.
var DesignPatterns = []string{
	//"Singleton",
	"Factory Method",
	"Abstract Factory",
	//"Builder",
	"Prototype",
	"Adapter",
	"Bridge",
	//"Composite",
	//"Decorator",
	"Facade",
	"Flyweight",
	//"Proxy",
	//"Chain of Responsibility",
	//"Command",
	//"Iterator",
	//"Mediator",
	"Memento",
	//"Observer",
// 	"State",
// 	"Strategy",
	//"Template Method",
	//"Visitor",
}

func main() {
	// Seed the random number generator to ensure different results each time
	rand.Seed(time.Now().UnixNano())

	// Pick a random index from the DesignPatterns slice
	randomIndex := rand.Intn(len(DesignPatterns))

	// Output the randomly chosen design pattern
	fmt.Println("Randomly selected design pattern:", DesignPatterns[randomIndex])
}
