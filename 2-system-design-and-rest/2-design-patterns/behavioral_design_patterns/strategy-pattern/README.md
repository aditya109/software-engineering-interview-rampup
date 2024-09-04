# Strategy Pattern 

It lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.


### Basic Structure

<image src="https://github.com/aditya109/software-engineering-interview-rampup/blob/main/2-system-design-and-rest/2-design-patterns/assets/strategy-pattern.png?raw=true"/>

### Example

```go
package main

import "fmt"

type EvictionAlgo interface {
	evict(c *Cache)
}

type Cache struct {
	storage      map[string]string
	evictionAlgo EvictionAlgo
	capacity     int
	maxCapacity  int
}

type Fifo struct{}

func (f *Fifo) evict(c *Cache) {
	fmt.Println("evicting by fifo strategy")
}

type Lfu struct{}

func (l *Lfu) evict(c *Cache) {
	fmt.Println("evicting by lfu strategy")
}

type Lru struct{}

func (l *Lru) evict(c *Cache) {
	fmt.Println("evicting by lru strategy")
}

func initCache(e EvictionAlgo) *Cache {
	return &Cache{
		storage:      make(map[string]string),
		evictionAlgo: e,
		capacity:     0,
		maxCapacity:  2,
	}
}

func (c *Cache) setEvictionAlgo(e EvictionAlgo) {
	c.evictionAlgo = e
}

func (c *Cache) add(key, value string) {
	if c.capacity == c.maxCapacity {
		c.evict()
	}
	c.capacity++
	c.storage[key] = value
}

func (c *Cache) get(key string) {
	delete(c.storage, key)
}

func (c *Cache) evict() {
	c.evictionAlgo.evict(c)
	c.capacity--
}

func main() {
	lfu := &Lfu{}
	cache := initCache(lfu)

	cache.add("a", "1")
	cache.add("b", "2")
	cache.add("c", "3")

	lru := &Lru{}
	cache.setEvictionAlgo(lru)

	cache.add("d", "4")

	fifo := &Fifo{}
	cache.setEvictionAlgo(fifo)

	cache.add("e", "5")

}

```

## Where to apply ?

- When you want to use different variants of an algorithm within an object and be able to switch from one algorithm to another during runtime.
- When you have a lot of similar classes that only differ in the way they execute some behavior.
- To isolate the business logic of a class from the implementation details of algorithms that may not be as important in the context of that logic.
- When your class has a massive conditional statement that switches between different variants of the same algorithm.

### Pros

- You can swap algorithms used inside an object at runtime. 
- You can isolate the implementation details of an algorithm from the code that uses it. 
- You can replace inheritance with composition. 
- Open/Closed Principle. You can introduce new strategies without having to change the context.

### Cons

- If you only have a couple of algorithms, and they rarely change, there’s no real reason to overcomplicate the program with new classes and interfaces that come along with the pattern. 
- Clients must be aware of the differences between strategies to be able to select a proper one. 
- A lot of modern programming languages have functional type support that lets you implement different versions of an algorithm inside a set of anonymous functions. Then you could use these functions exactly as you’d have used the strategy objects, but without bloating your code with extra classes and interfaces.
