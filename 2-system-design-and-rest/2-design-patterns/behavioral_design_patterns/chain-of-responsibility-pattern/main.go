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
