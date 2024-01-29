package main

import (
	"fmt"
	"sync"
)

var lock = &sync.Mutex{}

type single struct{}

var singleInstance *single

func getInstance(instance int) *single {
	if singleInstance == nil {
		lock.Lock()
		defer lock.Unlock()
		if singleInstance == nil {
			fmt.Println(instance, " -> Creating single instance now.")
			singleInstance = &single{}
		} else {
			fmt.Println(instance, " -> Single instance already created.")
		}

	} else {
		fmt.Println(instance, " -> Single instance already created.")
	}

	return singleInstance
}

func main() {
	for i := 0; i < 30; i++ {
		go getInstance(i)
	}
	fmt.Scanln()

}
