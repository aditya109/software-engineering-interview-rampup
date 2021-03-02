# What is a `Trie` ?

A data structure for storing items (usually strings) based off of prefixes the items share in common.

- Imagine if we want to store the words "wait", "waiter", "shop", "shopkeeper", etc.

![](D:\Work\go-workspace\src\github.com\aditya109\grokking-the-coding-interview\basics\trie\trie.png)

Time complexity to check if word "shopper" is in each data structure.

Trie -> O(M) where M is the length of "shopper"

Adding a word to a Trie takes O(M) time where M is the length of word to be added

## Building a Trie

### Implementation of Trie #1

```python
class Trie:
    def __init__(self) -> None:
        self.root = {"*": "*"}

    def add_word(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        current_node["*"] = "*"

    def does_not_exist(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return "*" in current_node
```

Using the above data structure,

```python
trie = Trie()
words = ["wait", "waiter", "shop", "shopkeeper"]
for word in words:
    trie.add_word(word)

print(trie.does_not_exist("wait"))
print(trie.does_not_exist(""))
print(trie.does_not_exist("waite"))
print(trie.does_not_exist("shop"))
print(trie.does_not_exist("shopp"))
```

### Implementation of Trie #2

```python
class TrieNode:
    def __init__(self, letter) -> None:
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def add_word(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode(letter)
            current_node = current_node.children[letter]
        current_node.is_end_of_word = True

    def does_word_exist(self, word):
        if word == "":
            return True
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]
        return current_node.is_end_of_word
```

Using the above data structure,

```python
trie = Trie()
words = ["wait", "waiter", "shop", "shopkeeper"]
for word in words:
    trie.add_word(word)

print(trie.does_word_exist("wait"))
print(trie.does_word_exist(""))
print(trie.does_word_exist("waite"))
print(trie.does_word_exist("shop"))
print(trie.does_word_exist("shopp"))
```

