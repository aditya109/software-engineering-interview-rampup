package builder_pattern

import "testing"

func TestBuilderPattern(t *testing.T) {
	manufacturingComplex := ManufacturingDirector{}

	carBuilder := &CarBuilder{}
	manufacturingComplex.SetBuilder(carBuilder)
	manufacturingComplex.Construct()

	car := carBuilder.GetVehicle()

	if car.Wheels != 4 {
		t.Errorf("wheels on a car must be 4 and they were %d\n", car.Wheels)
	}
	if car.Structure != "Car" {
		t.Errorf("structure on a car must be 'Car' and they were %s\n", car.Structure)
	}
	if car.Seats != 5 {
		t.Errorf("seats on a car must be 5 and they were %d\n", car.Seats)
	}

	bikeBuilder := &BikeBuilder{}
	manufacturingComplex.SetBuilder(bikeBuilder)
	manufacturingComplex.Construct()

	bike := bikeBuilder.GetVehicle()

	if bike.Wheels != 2 {
		t.Errorf("wheels on a bike must be 2 and they were %d\n", bike.Wheels)
	}
	if bike.Structure != "Bike" {
		t.Errorf("structure on a bike must be 'Bike' and they were %s\n", bike.Structure)
	}
	if bike.Seats != 2 {
		t.Errorf("seats on a bike must be 2 and they were %d\n", bike.Seats)
	}
}
