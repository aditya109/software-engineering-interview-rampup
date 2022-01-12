# Hashing

Collision Resolution techniques:

- Separate Chaining
- Open Addressing

## Separate Chaining

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2015/07/hashChaining1.png)

**Advantages:** 
1) Simple to implement. 
2) Hash table never fills up, we can always add more elements to the chain. 
3) Less sensitive to the hash function or load factors. 
4) It is mostly used when it is unknown how many and how frequently keys may be inserted or deleted. 

**Disadvantages:** 
1) Cache performance of chaining is not good as keys are stored using a linked list. Open addressing provides better cache performance as everything is stored in the same table. 
2) Wastage of Space (Some Parts of hash table are never used) 
3) If the chain becomes long, then search time can become O(n) in the worst case. 
4) Uses extra space for links. 

**Performance of Chaining:** 
Performance of hashing can be evaluated under the assumption that each key is equally likely to be hashed to any slot of table (simple uniform hashing). 

```
 m = Number of slots in hash table
 n = Number of keys to be inserted in hash table
 
 Load factor α = n/m 
  
 Expected time to search = O(1 + α)
 
 Expected time to delete = O(1 + α)

Time to insert = O(1)

 Time complexity of search insert and delete is 
 O(1) if  α is O(1)
```

## Open Addressing

Like separate chaining, open addressing is a method for handling collisions. In Open Addressing, all elements are stored in the hash table itself. So at any point, the size of the table must be greater than or equal to the total number of keys (Note that we can increase table size by copying old data if needed). 

Insert(k): Keep probing until an empty slot is found. Once an empty slot is found, insert k. 

Search(k): Keep probing until slot’s key doesn’t become equal to k or an empty slot is reached. 

Delete(k): ***Delete operation is interesting***. If we simply delete a key, then the search may fail. So slots of deleted keys are marked specially as “deleted”. 
The insert can insert an item in a deleted slot, but the search doesn’t stop at a deleted slot. 

Open Addressing is done in the following ways: 

***a) Linear Probing:*** In linear probing, we linearly probe for next slot. For example, the typical gap between two probes is 1 as seen in the example below.

Let **hash(x)** be the slot index computed using a hash function and **S** be the table size 

```
If slot hash(x)mod TableSize is full, then we try (hash(x) + 1)mod TableSize
If (hash(x) + 1)mod TableSize is also full, then we try (hash(x) + 2)mod TableSize
If (hash(x) + 2)mod TableSize is also full, then we try (hash(x) + 3)mod TableSize 
..................................................
..................................................
```

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2015/08/openAddressing1.png)



**Challenges in Linear Probing :**

1. **Primary Clustering:** One of the problems with linear probing is Primary clustering, many consecutive elements form groups and it starts taking time to find a free slot or to search for an element. 
2. **Secondary Clustering**: Secondary clustering is less severe, two records only have the same collision chain (Probe Sequence) if their initial position is the same.

***b) Quadratic Probing*** We look for i<sup>2th</sup> slot in i<sup>th</sup> iteration. 

```
let hash(x) be the slot index computed using hash function.  
If slot hash(x)mod TableSize is full, then we try (hash(x) + 1*1)mod TableSize
If (hash(x) + 1*1)mod TableSize is also full, then we try (hash(x) + 2*2)mod TableSize
If (hash(x) + 2*2)mod TableSize is also full, then we try (hash(x) + 3*3)mod TableSize
..................................................
..................................................
```

**c)** ***Double Hashing*** We use another hash function hash2(x) and look for i*hash2(x) slot in i<sup>th</sup> rotation. 

```
let hash(x) be the slot index computed using hash function.  
If slot hash(x)mod TableSize is full, then we try (hash(x) + 1*hash2(x))mod TableSize
If (hash(x) + 1*hash2(x))mod TableSize is also full, then we try (hash(x) + 2*hash2(x))mod TableSize
If (hash(x) + 2*hash2(x))mod TableSize is also full, then we try (hash(x) + 3*hash2(x))mod TableSize
..................................................
..................................................
```

**Performance of Open Addressing:** 

Like Chaining, the performance of hashing can be evaluated under the assumption that each key is equally likely to be hashed to any slot of the table (simple uniform hashing) 

```
m = Number of slots in the hash table
n = Number of keys to be inserted in the hash table
 
Load factor α = n/m  ( < 1 )

Expected time to search/insert/delete < 1/(1 - α) 

So Search, Insert and Delete take (1/(1 - α)) time
```

**d) Random Probing**

```
Randomize(X)
h0(X) = Hash(X)
h1(X) = (h0(x) + RandomGen()) mod TableSize
h2(X) = (h1(x) + RandomGen()) mod TableSize
```

### How hashing works:

For **insertion** of a key(K) – value(V) pair into a hash map, 2 steps are required:

1. K is converted into a small integer (called its hash code) using a hash function.
2. The hash code is used to find an index `(hashCode % arrSize)` and the entire linked list at that index(Separate chaining) is first searched for the presence of the K already.
3. If found, it’s value is updated and if not, the K-V pair is stored as a new node in the list.

### Complexity and Load Factor

- For the **first step**, time taken depends on the K and the hash function.
  For example, if the key is a string “`abcd`”, then it’s hash function may depend on the length of the string. But for very large values of n, the number of entries into the map, length of the keys is almost negligible in comparison to n so hash computation can be considered to take place in constant time, i.e, **O(1)**.
- For the **second step**, traversal of the list of K-V pairs present at that index needs to be done. For this, the worst case may be that all the n entries are at the same index. So, time complexity would be **O(n)**. But, enough research has been done to make hash functions uniformly distribute the keys in the array so this almost never happens.
- So, **on an average**, if there are n entries and b is the size of the array there would be n/b entries on each index. This value n/b is called the **load factor** that represents the load that is there on our map.
- This Load Factor needs to be kept low, so that number of entries at one index is less and so is the complexity almost constant, i.e., O(1).

### Rehashing:

As the name suggests, **rehashing means hashing again**. Basically, when the load factor increases to more than its pre-defined value (default value of load factor is 0.75), the complexity increases. So to overcome this, the size of the array is increased (doubled) and all the values are hashed again and stored in the new double sized array to maintain a low load factor and low complexity.

##### Why rehashing?

Rehashing is done because whenever key value pairs are inserted into the map, the load factor increases, which implies that the time complexity also increases as explained above. This might not give the required time complexity of O(1).

Hence, rehash must be done, increasing the size of the `bucketArray` so as to reduce the load factor and the time complexity.

##### How Rehashing is done?

Rehashing can be done as follows:

- For each addition of a new entry to the map, check the load factor.
- If it’s greater than its pre-defined value (or default value of 0.75 if not given), then Rehash.
- For Rehash, make a new array of double the previous size and make it the new bucketarray.
- Then traverse to each element in the old bucketArray and call the insert() for each so as to insert it into the new larger bucket array.



