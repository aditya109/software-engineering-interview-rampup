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
