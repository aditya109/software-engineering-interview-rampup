# Chain of Responsibility

## What is it ??

It lets you pass requests along a chain of handlers. 
Upon receiving a request, each handler decides either to process the request or to pass it to next handler in the chain.

### Basic Structure

<image src="https://github.com/aditya109/software-engineering-interview-rampup/blob/main/2-system-design-and-rest/2-design-patterns/assets/chain-of-responsibility-pattern.png?raw=true"/>


### Example

```go
package main

import "fmt"

type Patient struct {
	name                                                                   string
	isRegistrationDone, isDoctorCheckUpDone, isMedicineDone, isPaymentDone bool
}

type Department interface {
	execute(*Patient)
	setNext(Department)
}

type Reception struct {
	next Department
}

func (r *Reception) execute(p *Patient) {
	if p.isRegistrationDone {
		fmt.Println("Patient registration already done")
		r.next.execute(p)
		return
	}
	fmt.Println("Reception registering patient")
	p.isRegistrationDone = true
	r.next.execute(p)
}

func (r *Reception) setNext(next Department) {
	r.next = next
}

type Doctor struct {
	next Department
}

func (d *Doctor) execute(p *Patient) {
	if p.isDoctorCheckUpDone {
		fmt.Println("Patient doctor checkup already done")
		d.next.execute(p)
		return
	}
	fmt.Println("Doctor checking patient")
	p.isDoctorCheckUpDone = true
	d.next.execute(p)
}

func (d *Doctor) setNext(next Department) {
	d.next = next
}

type Medical struct {
	next Department
}

func (m *Medical) execute(p *Patient) {
	if p.isMedicineDone {
		fmt.Println("Medicine is already given to patient")
		m.next.execute(p)
		return
	}
	fmt.Println("Medical is giving medicine to patient")
	p.isMedicineDone = true
	m.next.execute(p)
}

func (m *Medical) setNext(next Department) {
	m.next = next
}

type Cashier struct {
	next Department
}

func (c *Cashier) execute(p *Patient) {
	if p.isPaymentDone {
		fmt.Println("Patient payment already done")
	}
	fmt.Println("Cashier getting money from patient patient")
}

func (c *Cashier) setNext(next Department) {
	c.next = next
}

func main() {
	cashier := &Cashier{}

	medical := &Medical{}
	medical.setNext(cashier)

	doctor := &Doctor{}
	doctor.setNext(medical)

	reception := &Reception{}
	reception.setNext(doctor)

	patient := &Patient{name: "abc"}
	reception.execute(patient)
}

```

### Where to apply ?

- When your program is expected to process different kinds of requests in various ways, but the exact types of requests and their sequences are unknown beforehand.
- When it’s essential to execute several handlers in a particular order.
- When the set of handlers and their order are supposed to change at runtime.

#### Pros

- You can control the order of request handling.
- Single Responsibility Principle. You can decouple classes that invoke operations from classes that perform operations.
- Open/Closed Principle. You can introduce new handlers into the app without breaking the existing client code.

#### Cons
- Some requests may end up unhandled.
