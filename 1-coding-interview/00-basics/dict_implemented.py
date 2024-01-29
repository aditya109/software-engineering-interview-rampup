from typing import Any


class HashTable:
    hashmap: list[list[Any]]

    def __init__(self):
        self.size = 20
        self.hashmap = [[] for _ in range(self.size)]

    def __str__(self):
        return str(self.hashmap)

    def hashing_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    def set(self, key, value):
        hash_key = self.hashing_func(key)
        key_exist = False
        slot = self.hashmap[hash_key]

        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exist = True
                break
        if key_exist:
            slot[i] = (key, value)
        else:
            slot.append((key, value))

    def get(self, key):
        hash_key = self.hashing_func(key)
        slot = self.hashmap[hash_key]

        for kv in slot:
            k, v = kv
            if key == k:
                return v
            else:
                raise KeyError('does not exist')

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)


h = HashTable()
h.set('key1', 'value1')
h.set('key4', 'value5')
h.set('key2', 'value2')
h.set('key3', 'value3')

print(h.get('key1'))

h['key4'] = 'value4'
print(h)
