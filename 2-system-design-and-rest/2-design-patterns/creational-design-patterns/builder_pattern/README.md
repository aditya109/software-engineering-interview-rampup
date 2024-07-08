# Builder Design Pattern
- Helps to construct complex objects without directly instantiating their struct
- Avoid writing the logic to create all the object in the package 
- Helps us maintain an unpredictable number of products
- Newcomer to source code can add a new product to the pipeline
- `BuildProcess` interface specifies what one must comply to be part of the possible builder

## Use-cases:
- Instance creation can be simple or complex, an object can be composed of many objects, one can use the same technique to create many types of objects.

## Objectives:
- abstract complex creations are required
- create an object step by step by filling its field and creating embedded objects
- reuse the object creation algorithm between many objects

## When to use:
- can be used when all the builders implement all the underlying object creation methods
- when underlying implementation is simpler and stable

## Applicability

1. Use the Builder pattern to get rid of a `telescoping constructor`

- 