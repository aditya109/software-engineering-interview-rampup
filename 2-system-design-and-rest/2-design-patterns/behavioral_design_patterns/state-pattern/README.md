# State Pattern

## What is it ?

It lets an object alter its behaviour when its internal state changes. It appears as if the object changes its class.  

### Basic Structure

<image src="https://github.com/aditya109/software-engineering-interview-rampup/blob/main/2-system-design-and-rest/2-design-patterns/assets/state-pattern.png?raw=true"/>


### Example

```go
package main

import (
	"fmt"
	"log"
)

type State interface {
	addItem(int) error
	requestItem() error
	insertMoney(money int) error
	dispenseItem() error
}

// HasMoneyState state definition
type HasMoneyState struct {
	vendingMachine *VendingMachine
}

func (h *HasMoneyState) addItem(i int) error {
	return fmt.Errorf("item dispense in progress")
}
func (h *HasMoneyState) requestItem() error {
	return fmt.Errorf("item dispense in progress")
}
func (h *HasMoneyState) insertMoney(money int) error {
	return fmt.Errorf("item out of stock")
}
func (h *HasMoneyState) dispenseItem() error {
	fmt.Println("dispensing item")
	h.vendingMachine.itemCount -= 1
	if h.vendingMachine.itemCount == 0 {
		h.vendingMachine.setState(h.vendingMachine.noItem)
	} else {
		h.vendingMachine.setState(h.vendingMachine.hasItem)
	}
	return nil
}

// ItemRequestedState state definition
type ItemRequestedState struct {
	vendingMachine *VendingMachine
}

func (i *ItemRequestedState) addItem(count int) error {
	return fmt.Errorf("item already requested")
}
func (i *ItemRequestedState) requestItem() error {
	return fmt.Errorf("item already requested")
}
func (i *ItemRequestedState) insertMoney(money int) error {
	if money < i.vendingMachine.itemPrice {
		return fmt.Errorf("inserted money is less. Please insert %d", i.vendingMachine.itemPrice)
	}
	fmt.Println("Money entered is ok")
	i.vendingMachine.setState(i.vendingMachine.hasMoney)
	return nil
}
func (i *ItemRequestedState) dispenseItem() error {
	return fmt.Errorf("please insert money first")
}

// HasItemState state definition
type HasItemState struct {
	vendingMachine *VendingMachine
}

func (i *HasItemState) requestItem() error {
	if i.vendingMachine.itemCount == 0 {
		i.vendingMachine.setState(i.vendingMachine.noItem)
		return fmt.Errorf("no item present")
	}
	fmt.Printf("Item requestd\n")
	i.vendingMachine.setState(i.vendingMachine.itemRequested)
	return nil
}
func (i *HasItemState) addItem(count int) error {
	fmt.Printf("%d items added\n", count)
	i.vendingMachine.incrementItemCount(count)
	return nil
}
func (i *HasItemState) insertMoney(money int) error {
	return fmt.Errorf("please select item first")
}
func (i *HasItemState) dispenseItem() error {
	return fmt.Errorf("please select item first")
}

// NoItemState state definition
type NoItemState struct {
	vendingMachine *VendingMachine
}

func (i *NoItemState) requestItem() error {
	return fmt.Errorf("item out of stock")
}

func (i *NoItemState) addItem(count int) error {
	i.vendingMachine.incrementItemCount(count)
	i.vendingMachine.setState(i.vendingMachine.hasItem)
	return nil
}

func (i *NoItemState) insertMoney(money int) error {
	return fmt.Errorf("item out of stock")
}
func (i *NoItemState) dispenseItem() error {
	return fmt.Errorf("item out of stock")
}

// VendingMachine represents Vending Machine
type VendingMachine struct {
	hasItem, itemRequested, hasMoney, noItem, currentState State
	itemCount, itemPrice                                   int
}

func newVendingMachine(itemCount, itemPrice int) *VendingMachine {
	v := &VendingMachine{
		itemCount: itemCount,
		itemPrice: itemPrice,
	}
	hasItemState := &HasItemState{
		vendingMachine: v,
	}
	itemRequestedState := &ItemRequestedState{
		vendingMachine: v,
	}
	hasMoneyState := &HasMoneyState{
		vendingMachine: v,
	}
	noItemState := &NoItemState{
		vendingMachine: v,
	}

	v.setState(hasItemState)
	v.hasItem = hasItemState
	v.itemRequested = itemRequestedState
	v.hasMoney = hasMoneyState
	v.noItem = noItemState
	return v
}
func (v *VendingMachine) requestItem() error {
	return v.currentState.requestItem()
}
func (v *VendingMachine) addItem(count int) error {
	return v.currentState.addItem(count)
}
func (v *VendingMachine) insertMoney(money int) error {
	return v.currentState.insertMoney(money)
}
func (v *VendingMachine) dispenseItem() error {
	return v.currentState.dispenseItem()
}
func (v *VendingMachine) setState(s State) {
	v.currentState = s
}
func (v *VendingMachine) incrementItemCount(count int) {
	fmt.Printf("Adding %d items\n", count)
	v.itemCount = v.itemCount + count
}

func main() {
	vendingMachine := newVendingMachine(1, 10)

	err := vendingMachine.requestItem()
	if err != nil {
		log.Fatalf(err.Error())
	}

	err = vendingMachine.insertMoney(10)
	if err != nil {
		log.Fatalf(err.Error())
	}

	err = vendingMachine.dispenseItem()
	if err != nil {
		log.Fatalf(err.Error())
	}

	fmt.Println()

	err = vendingMachine.addItem(2)
	if err != nil {
		log.Fatalf(err.Error())
	}

	fmt.Println()

	err = vendingMachine.requestItem()
	if err != nil {
		log.Fatalf(err.Error())
	}

	err = vendingMachine.insertMoney(10)
	if err != nil {
		log.Fatalf(err.Error())
	}

	err = vendingMachine.dispenseItem()
	if err != nil {
		log.Fatalf(err.Error())
	}
}

```

## Where to apply ?
- When you have an object that behaves differently depending on its current state, the number of states is enormous, and the state-specific code changes frequently.
- When you have a class polluted with massive conditionals that alter how the class behaves according to the current values of the class’s fields.
- When you have a lot of duplicate code across similar states and transitions of a condition-based state machine.

### Pros
- Single Responsibility Principle. Organize the code related to particular states into separate classes.
- Open/Closed Principle. Introduce new states without changing existing state classes or the context.
- Simplify the code of the context by eliminating bulky state machine conditionals.

### Cons
- Applying the pattern can be overkill if a state machine has only a few states or rarely changes.

