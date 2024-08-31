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
