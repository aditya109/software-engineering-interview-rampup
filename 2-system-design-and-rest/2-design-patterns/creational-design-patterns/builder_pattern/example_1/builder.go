package builder_pattern

/*
Create a Vehicle manufacturing program

- create relationship between a director, a few builders and the product they build
- every kind of vehicle, chosse vehicle type, assemble the structure, place the wheels and place the seats.
- director is represented by the manufacturing director type

Requirements and acceptance criteria
- you must have a manufacturing type
- VehicleProduct with 4 wheels, 5 seats and a structure defined as car must be returned
- VehicleProduct with 2 wheels, 2 seats and a structure defined as a motorbike must be returned
- VehicleProduct built by any BuildProcess builder must be open to modifications
*/

type BuildProcess interface {
	SetWheels() BuildProcess
	SetSeats() BuildProcess
	SetStructure() BuildProcess
	GetVehicle() VehicleProduct
}

// director
type ManufacturingDirector struct {
	builder BuildProcess
}

func (f *ManufacturingDirector) Construct() {
	f.builder.SetSeats().SetStructure().SetWheels()
}

func (f *ManufacturingDirector) SetBuilder(b BuildProcess) {
	f.builder = b
}

// product
type VehicleProduct struct {
	Wheels    int
	Seats     int
	Structure string
}

// builder of type car
type CarBuilder struct {
	v VehicleProduct
}

func (c *CarBuilder) GetVehicle() VehicleProduct {
	return c.v
}

func (c *CarBuilder) SetSeats() BuildProcess {
	c.v.Seats = 5
	return c
}

func (c *CarBuilder) SetStructure() BuildProcess {
	c.v.Structure = "Car"
	return c
}

func (c *CarBuilder) SetWheels() BuildProcess {
	c.v.Wheels = 4
	return c
}

type BikeBuilder struct {
	v VehicleProduct
}

func (b *BikeBuilder) GetVehicle() VehicleProduct {
	return b.v
}

func (b *BikeBuilder) SetSeats() BuildProcess {
	b.v.Seats = 2
	return b
}

func (b *BikeBuilder) SetStructure() BuildProcess {
	b.v.Structure = "Bike"
	return b
}

func (b *BikeBuilder) SetWheels() BuildProcess {
	b.v.Wheels = 2
	return b
}
