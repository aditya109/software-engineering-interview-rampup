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
