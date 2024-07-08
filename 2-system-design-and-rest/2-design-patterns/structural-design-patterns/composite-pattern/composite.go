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
