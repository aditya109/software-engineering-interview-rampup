package main

import "fmt"

type IPizza interface {
	getPrice() int
}

type VeggieMania struct {
}

func (p *VeggieMania) getPrice() int {
	return 15
}

// TomatoTopping concrete decorator
type TomatoTopping struct {
	pizza IPizza
}

func (t *TomatoTopping) getPrice() int {
	pizzaPrice := t.pizza.getPrice()
	return pizzaPrice + 7
}

// CheeseTopping concrete decorator
type CheeseTopping struct {
	pizza IPizza
}

func (t *CheeseTopping) getPrice() int {
	pizzaPrice := t.pizza.getPrice()
	return pizzaPrice + 10
}

func main() {
	pizza := &VeggieMania{}

	pizzaWithCheese := &CheeseTopping{pizza}
	pizzaWithTomato := &TomatoTopping{pizza}

	fmt.Printf("price of pizza with cheese topping is ₹ %d and that of prizza with tomato topping is ₹ %d\n", pizzaWithCheese.getPrice(), pizzaWithTomato.getPrice())
}
