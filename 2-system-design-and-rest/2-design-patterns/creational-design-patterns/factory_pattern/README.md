# Factory Design Pattern
- delegates the creation of different type of instances
- abstracts the user from the knowledge of the struct he needs to achieve 
- provides an interface that fits the user needs
- eases the process of downgrading or upgrading of the implementation

## Usecases:
- we gain an extra layer of encapsulation as program grows in a controlled environment
- we can delegate the creation of families of objects to a different package

## Objectives:
- delegating the creation of new instances of structures
- working at the interface level instead concrete implementations
- grouping families of objects to obtain a family object creator

## When to use:
- grouping families of objects is needed
- upgrading an implementation of used structs is required

