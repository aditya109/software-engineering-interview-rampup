package main

import "fmt"

type TrieNode struct {
	children    map[rune]*TrieNode
	isEndOfWord bool
}

func NewTrieNode() *TrieNode {
	return &TrieNode{make(map[rune]*TrieNode), false}
}

type Trie struct {
	root *TrieNode
}

func NewTrie() *Trie {
	return &Trie{NewTrieNode()}
}

func (t *Trie) Insert(word string) {
	cur := t.root

	for _, ch := range word {
		if _, exists := cur.children[ch]; !exists {
			cur.children[ch] = NewTrieNode()
		}
		cur = cur.children[ch]
	}
	cur.isEndOfWord = true
}

func (t *Trie) Search(word string) bool {
	cur := t.root

	for _, ch := range word {
		if _, exists := cur.children[ch]; !exists {
			return false
		}
		cur = cur.children[ch]
	}
	return cur.isEndOfWord
}

func (t *Trie) StartsWith(prefix string) bool {
	cur := t.root
	for _, ch := range prefix {
		if _, exists := cur.children[ch]; !exists {
			return false
		}
		cur = cur.children[ch]
	}
	return true
}

func main() {
	trie := NewTrie()
	trie.Insert("hello")
	fmt.Println(trie.Search("hello"))    // true
	fmt.Println(trie.Search("hell"))     // false
	fmt.Println(trie.StartsWith("hell")) // true
	fmt.Println(trie.StartsWith("helloa"))
}
