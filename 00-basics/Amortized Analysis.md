# Amortized Analysis

Time Complexity averaged over an extended period of time.

```
a = [] # size 10
Keep inserting till size(a) is 10
If you insert more, we don't have more space.
What we can do is take a new array of size = 2 * size(a).
Copy all the elements of previous array a into new array. Replace the old reference of a by new reference of freshlt copied array, and then insert a new element.
```

**Amortized time** is the way to express the **time complexity** when an algorithm has the very bad **time complexity** only once in a while besides the **time complexity** that happens most of **time**.

Let's calculate the time complexity normally for the insertion of the Array.

For worst-case scenario, let's say we have to insert n elements into the array and the array-size is maxed out.

Cost of insertion:

- `O(1)`
- Doubling cost (`2*size`) + Copying the old array cost (size)= `3*size` 

Since it is a worst-case time complexity, the cost will be `n * 3*N` = O(N<sup>2</sup>)

But let's analyze it further.

Let's say my initial array size is 1.We insert `1` into the array. `O(1)`

Now we want to insert `2` into the array. We have to perform doubling + copying + insertion. `O(2 + 1 + 1)`

Now again we want to insert `3` into the array.  We have to perform doubling + copying + insertion. `O(4 + 2 + 1)`

Now again we want to insert `4` into the array.  We have to perform insertion. `O(1)`

Now again we want to insert `5` into the array.  We have to perform doubling + copying + insertion. `O(8 + 4 + 1)`.

Now again we want to insert `6`, `7` and `8` into the array. We just have to perform insertion. `O(1)`

Now again if want to insert `9` into the array, we will have to perform doubling + copying + insertion. `O(16 + 8 + 1)`

What we can conclude is we are doing cheaper operations, far more frequently than the expensive operations.

The resizing will happen only at operation 1, 2, 4, …, 2k, for a total of 1 + 2 + 4 + …+ 2k = 2·2k - 1 constant-time element copy operations. Since 2k ≤ *n*, this is at most 2*n* - 1.

> GP sum = **a[(r<sup>n</sup>-1)/(r-1)] if r ≠ 1**

Also, every time we double + copy, we are doing `3*size + 1` work.

Trying to be accurate for the worst time complexity, if the internal array capacity starts with 1, then the capacities will be `1, 2, 4, 8, 16,...., X` when it hits the capacity and gets doubled. It takes `1, 2, 4, 8, 16,...., X` items to copy into the new array depending on the capacity that has been reached. So the time complexity will be `1 + 2 + 4 + 8 + 16 + … + X`. If you think from X, this will be`X + X/2 + X/4 + X/8 + … + 1 = 2X` approximately.

> **The insertion takes O(2X)** when the capacity of X has been reached, **and the amortized time for each insertion is O(1).**

