package singleton_pattern

/**
Create a unique counter
 
- When no counter has been created before, a new one is created with the value 0
- If a counter has already been created, return this instance that holds actual count
- If we call the method addOne, the count must be incremented by 1

*/ 



type Singleton interface {
	AddOne() int
}

type singleton struct {
	count int
}

var instance *singleton

func GetInstance() Singleton {
	if instance == nil {
		instance = new(singleton)
	}
	return instance
}

func (s *singleton) AddOne() int {
	s.count++
	return s.count
}
