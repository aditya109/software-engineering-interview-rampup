package main

import (
	"fmt"
	"sync"
)

var once sync.Once

type single struct {
}

var singleInstance *single

func getInstance(instance int) *single {
	if singleInstance == nil {
		once.Do(
			func() {
				fmt.Println(instance, " -> Creating single instance now.")
				singleInstance = &single{}
			})
	} else {
		fmt.Println(instance, " -> Single instance already created.")
	}

	return singleInstance
}
func main() {
	var wg sync.WaitGroup
	for i := 0; i < 30; i++ {
		fmt.Println("running iteration: ", i)
		wg.Add(1)
		go func() {
			defer wg.Done()
			getInstance(i)
		}()
	}
	wg.Wait()
}
