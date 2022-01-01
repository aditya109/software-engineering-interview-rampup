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


trie = Trie()
words = ["wait", "waiter", "shop", "shopkeeper"]
for word in words:
    trie.add_word(word)

print(trie.does_not_exist("wait"))
print(trie.does_not_exist(""))
print(trie.does_not_exist("waite"))
print(trie.does_not_exist("shop"))
print(trie.does_not_exist("shopp"))
