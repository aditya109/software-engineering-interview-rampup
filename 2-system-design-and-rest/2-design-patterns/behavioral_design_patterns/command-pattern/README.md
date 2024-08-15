# Command Design Pattern

## What is it ?


### Basic Structure

<img src="../../assets/command-pattern.svg"></img>

```go
package main

import "fmt"

type Command interface {
	execute()
}

type Button struct {
	command Command
}

func (b *Button) press() {
	b.command.execute()
}

type Device interface {
	on()
	off()
}

type OffCommand struct {
	device Device
}

func (o *OffCommand) execute() {
	o.device.off()
}

type OnCommand struct {
	device Device
}

func (o *OnCommand) execute() {
	o.device.on()
}

type Tv struct {
	isRunning bool
}

func (t *Tv) on() {
	t.isRunning = true
	fmt.Println("TV is running")
}

func (t *Tv) off() {
	t.isRunning = false
	fmt.Println("TV is off")
}

// Client code

func main() {
	tv := &Tv{}

	onCommand := &OnCommand{
		device: tv,
	}
	offCommand := &OffCommand{
		device: tv,
	}
	onButton := &Button{
		command: onCommand,
	}
	onButton.press()
	offButton := &Button{
		command: offCommand,
	}
	offButton.press()
}

```

The output found:

```shell
TV is running
TV is off
```


## When to apply ?

1. When you want to parametrize objects with operations.
2. When you want to queue operations, schedule their execution or execute them remotely.
3. When you want to implement reversible operations.


## Pros

1. Open-closed principle.
2. Single responsibility principle.
3. You can implement undo/redo.
4. You can implement deferred execution of operations.
5. You can assemble a set of simple commands into a complex one.

## Cons

1. The code may become more complicated since you're introducing a whole new layer between senders and receivers.