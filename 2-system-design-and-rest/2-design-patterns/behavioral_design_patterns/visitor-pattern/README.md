# Composite Design Pattern

## What is it ?


### Basic Structure

<img src="../../assets/visitor-pattern.svg"></img>

### Example

<img src="../../assets/example-visitor-pattern.svg"></img>

```go
package main

import "fmt"

type Visitor interface {
	visitForSquare(*Square)
	visitForCircle(*Circle)
	visitForRectangle(*Rectangle)
}

type Shape interface {
	getType() string
	accept(Visitor)
}

type Circle struct {
	radius int
}

func (c *Circle) getType() string {
	return "Circle"
}

func (c *Circle) accept(v Visitor) {
	v.visitForCircle(c)
}

type Rectangle struct {
	length  int
	breadth int
}

func (r *Rectangle) getType() string {
	return "Rectangle"
}

func (r *Rectangle) accept(v Visitor) {
	v.visitForRectangle(r)
}

type Square struct {
	side int
}

func (s *Square) getType() string {
	return "Square"
}

func (s *Square) accept(v Visitor) {
	v.visitForSquare(s)
}

type AreaCalculator struct {
	area int
}

func (a *AreaCalculator) visitForSquare(s *Square) {
	fmt.Println("calculating area for square")
}

func (a *AreaCalculator) visitForCircle(c *Circle) {
	fmt.Println("calculating area for circle")
}

func (a *AreaCalculator) visitForRectangle(r *Rectangle) {
	fmt.Println("calculating area for rectangle")
}

type MiddleCoordinates struct {
	x int
	y int
}

func (m *MiddleCoordinates) visitForSquare(s *Square) {
	fmt.Println("calculating middle coordinates for square")
}

func (m *MiddleCoordinates) visitForCircle(c *Circle) {
	fmt.Println("calculating middle coordinates for circle")
}

func (m *MiddleCoordinates) visitForRectangle(r *Rectangle) {
	fmt.Println("calculating middle coordinates for rectangle")
}

func main() {
	square := &Square{
		side: 4,
	}
	circle := &Circle{
		radius: 10,
	}
	rectangle := &Rectangle{
		length:  10,
		breadth: 5,
	}
	areaCalculator := &AreaCalculator{}

	square.accept(areaCalculator)
	circle.accept(areaCalculator)
	rectangle.accept(areaCalculator)

	fmt.Println()
	middleCoordinates := &MiddleCoordinates{}
	square.accept(middleCoordinates)
	circle.accept(middleCoordinates)
	rectangle.accept(middleCoordinates)
}

```

The output found:

```shell
calculating area for square
calculating area for circle
calculating area for rectangle

calculating middle coordinates for square
calculating middle coordinates for circle
calculating middle coordinates for rectangle
```


## When to apply ?

1. When cleaning up the business logic of auxiliary behaviours is required.
2. When a behaviour makes sense only in some classes of a class hierarchy, but not in others.

## Pros

1. Open-closed principle.
2. Single responsibility principle.
3. A visitor object can accumulate some useful information while working with various objects.

## Cons

1. All visitor classes need to be updated whenever a class is added/removed.