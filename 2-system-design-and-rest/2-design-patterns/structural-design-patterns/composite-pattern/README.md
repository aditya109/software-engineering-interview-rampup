# Composite Design Pattern

## What is it ?

Composite is a design pattern which lets you compose objects into tree structures and work with these structures as if they were individual objects.

It favors composition (HAS-A relationship) over inheritance (IS-A relationship).
It creates hierarchies and tree of objects.
Objects have different objects with their own fields and methods inside them.

### Basic Structure

<img src="../../assets/composite-pattern.svg"></img>

### Example

<img src="../../assets/example-composite-pattern.svg"></img>

```go
package main

import "fmt"

type Component interface {
	search(string) bool
}

type Folder struct {
	components []Component
	name       string
}

func (f *Folder) search(keyword string) bool {
	fmt.Printf("Searching recursively for keyword %s in folder %s \n\n", keyword, f.name)
	for _, composite := range f.components {
		if composite.search(keyword) {
			return true
		}
	}
	return false
}
func (f *Folder) add(c Component) {
	f.components = append(f.components, c)
}

type File struct {
	name string
}

func (f *File) search(keyword string) bool {
	fmt.Printf("Searching recursively for keyword %s in file \n", keyword)
	if f.name == keyword {
		return true
	}
	return false
}

func (f *File) getName() string {
	return f.name
}

func main() {
	file1 := &File{name: "file1"}
	file2 := &File{name: "file2"}
	file3 := &File{name: "file3"}
	file4 := &File{name: "file4"}

	folder1 := &Folder{
		name: "Folder1",
	}
	folder1.add(file1)
	folder2 := &Folder{
		name: "Folder2",
	}
	folder2.add(file2)
	folder2.add(file3)
	folder2.add(file4)
	if found := folder2.search("file4"); found {
		fmt.Println("file4 found")
	} else {
		fmt.Println("file4 not found")
	}
}
```
The output found:
```shell
Searching recursively for keyword file4 in folder Folder2 

Searching recursively for keyword file4 in file 
Searching recursively for keyword file4 in file 
Searching recursively for keyword file4 in file 
file4 found
```


## When to apply ?

1. Makes sense only if core model of your application can be represented into a tree.

## Pros

1. One can work with complex tree structures easily. (Polymorphism + recursion)
2. Open/closed principle

## Cons
1. Difficult to provide a common interface for classes whose functionality differs too much. Over-generalization.