# Decorator Pattern

## What is it ???

*Decorator* is a structural design pattern that lets you attach new behaviour to objects by placing these objects inside special wrapper objects that contain the behaviours.

### Basic Structure

<image src="https://github.com/aditya109/software-engineering-interview-rampup/blob/main/2-system-design-and-rest/2-design-patterns/assets/command-design-pattern.png?raw=true"/>

## Where to apply ?
- When you need to be able to assign extra behaviours to objects at runtime without breaking the code that uses these objects.
- Use this when its not possible to extend an object's behaviour using inheritance.

### Pros

- Can extend an object's behaviour without making a new subclass.
- You can add/remove responsibilities from an object at runtime.
- You can combine several behaviours by wrapping an object into multiple decorators.
- SRP

### Cons

- Difficult to remove a specific wrapper from wrapper stack.
- Different to implement a decorator in such a way that it does not depend on the order in the decorator stack.