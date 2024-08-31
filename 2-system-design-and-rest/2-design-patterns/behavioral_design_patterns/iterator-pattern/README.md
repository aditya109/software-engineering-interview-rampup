# Iterator Pattern

##  What is it ???

It lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

### Basic Structure

<image src="https://github.com/aditya109/software-engineering-interview-rampup/blob/main/2-system-design-and-rest/2-design-patterns/assets/iterator-pattern.png?raw=true"/>

### Example

```go
package main

import "fmt"

type User struct {
	name string
	age  int
}

type Iterator interface {
	hasNext() bool
	getNext() *User
}

type Collection interface {
	createIterator() Iterator
}

type UserIterator struct {
	index int
	users []*User
}

func (u *UserIterator) hasNext() bool {
	return u.index < len(u.users)
}

func (u *UserIterator) getNext() *User {
	if u.hasNext() {
		user := u.users[u.index]
		u.index++
		return user
	}
	return nil
}

type UserCollection struct {
	users []*User
}

func (u *UserCollection) createIterator() Iterator {
	return &UserIterator{
		users: u.users,
	}
}

func main() {
	user1 := &User{
		name: "a",
		age:  20,
	}

	user2 := &User{
		name: "b",
		age:  30,
	}

	userCollection := &UserCollection{
		users: []*User{user1, user2},
	}
	iterator := userCollection.createIterator()
	for iterator.hasNext() {
		user := iterator.getNext()
		fmt.Printf("user: %+v \n", user)
	}
}

```

## Where to apply ??

- When your collection has a complex data structure under the hood, but you want to hide its complexity from clients (either for convenience or security reasons).
- To reduce duplication of the traversal code across your app.
- When you want your code to be able to traverse different data structures or when types of these structures are unknown beforehand.

### Pros

- Single Responsibility Principle. You can clean up the client code and the collections by extracting bulky traversal algorithms into separate classes.
- Open/Closed Principle. You can implement new types of collections and iterators and pass them to existing code without breaking anything.
- You can iterate over the same collection in parallel because each iterator object contains its own iteration state.
- For the same reason, you can delay an iteration and continue it when needed.

### Cons

- Applying the pattern can be an overkill if your app only works with simple collections. 
- Using an iterator may be less efficient than going through elements of some specialized collections directly.