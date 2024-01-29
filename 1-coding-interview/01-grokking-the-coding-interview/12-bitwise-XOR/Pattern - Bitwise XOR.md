# Pattern - Bitwise XOR 

Exclusive-Or returns a bit value of 1 if both bits are of opposite (different) nature, otherwise Exclusive-OR returns 0. 

````
	0000		
  ^	0000
  -------
  	0000
==============================
  	1111		
  ^	0000
  -------
  	1111
==============================
  	1111		
  ^	1111
  -------
  	0000
==============================
  	1100		
  ^	1010
  -------
  	0110
````

 If you take XOR of a number with 0 (zero), it would return the same number again.

```
x = 4 => 100
y = 2 => 010

x ^ 0 => 100 ^ 000 => x
6 ^ 0 = 6
```

If you take XOR of a number with itself, it would return 0 (zero).

```psuedocode
x = 4 => 100
y = 2 => 010

x ^ x => 100 ^ 100 => 0
6 ^ 6 = 0
```

**Example:**

1. We can swap the values of two variables without using any third (temp).

   ```
   a = 5
   b = 10
   
   a = a ^ b (a = 5 ^ 10 = 15)
   b = a ^ b (b = 15 ^ 10 = 5)
   a = a ^ b (a = 15 ^ 5 = 10)
   ```

2. Toggling(flipping) the k-th bit (from right) of a binary number:

   ```
   Let  n = 27, k = 3
   we can use: n ^ (1 << (k-1))
   11011 ^ (00001 << 2)
   11011 ^ (00100)
   11111
   ```

3.  Find the missing number from the list of numbers:

   **Question:** You are given a list of `n-1` integers, and these integers are in the range of `1` to `n`. There are no duplicates in the list. One of the integers is missing in the list, now, we need to find that missing number.

   *<u>Method 1</u>* By finding sum of first `n` natural numbers.

   1. First, find the sum of all number from 1 to n.
   2. Subtract all the element of the given list from the sum, and we'll give the missing number.

   > There might be an integer overflow while adding large numbers.

   *<u>Method 2</u>* Using XOR operator

   1. Take the XOR of all numbers 1 to n.

   2. Take XOR of all elements of the given array.

   3. XOR of Step 1 and Step 2 will given the required the missing number.

      ```
      arr = [4, 2, 1, 6, 8, 5, 3, 9]
      n = 9
      
      step1_result = 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8 ^ 9
      step2_result = 4 ^ 2 ^ 1 ^ 6 ^ 8 ^ 5 ^ 3 ^ 9
      
      final_result = step1_result ^ step2_result = 7
      
      final_result 
      = (1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8 ^ 9) ^ (4 ^ 2 ^ 1 ^ 6 ^ 8 ^ 5 ^ 3 ^ 9) 
      = (1 ^ 1) ^ (2 ^ 2) ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5) ^ (6 ^ 6) ^ (7) ^ (8 ^ 8) ^ (9 ^ 9)
      = 0 ^ 0 ^ 0 ^ 0 ^ 0 ^ 0 ^ 7 ^ 0 ^ 0
      = 7 (required result)
      ```

   4. Construct an array from XOR of all elements of the array except element at same index.

      > Given an array A[] having `n` positive elements. The task is to create an another array B[] such as B[i] is XOR of all elements of the array A[] except A[i].

      *Method 1:* Using `XOR` operator `O(N)`

      1. Find XOR of all elements of the given array.
      2. Now, for each element of A[], calculate A[i] = step1_result ^ A[i]  

````
arr = [4, 1, 2, 6, 8, 5, 3, 9]
step1_result = 4 ^ 1 ^ 2 ^ 6 ^ 8 ^ 5 ^ 3 ^ 9
````

  