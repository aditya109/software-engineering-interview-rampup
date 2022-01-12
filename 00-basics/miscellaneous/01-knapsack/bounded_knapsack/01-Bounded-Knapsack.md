# Knapsack 

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

![knapsack-problem](https://media.geeksforgeeks.org/wp-content/cdn-uploads/knapsack-problem.png)

## Recursive

```python
def knapsack_r(arr, val, W, n):
    if n == 0 or W == 0:
        return 0

    if arr[n-1] <= W:
        return max(val[n-1] + knapsack_r(arr, val, W-val[n-1], n-1), knapsack_r(arr, val, W, n-1))
    else:
        return knapsack_r(arr, val, W, n-1)
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]

W = 7
n = 4
print(knapsack_r(wt, val, W, n))
```

## Memoization

```python
t = [[0 if i == 0 or j == 0 else -
          1 for j in range(W+1)] for i in range(n+1)]

def knapsack_m(arr, val, W, n):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    if arr[n-1] <= W:
        t[n][W] = max(val[n-1] + knapsack_m(arr, val, W-val[n-1], n-1), knapsack_m(arr, val, W, n-1))
        return t[n][W]
    else:
        t[n][W] = knapsack_m(arr, val, W, n-1)
        return t[n][W]
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]

W = 7
n = 4
print(knapsack_m(wt, val, W, n))
```

## Top Down Approach

```python
t = [[0 if i == 0 or j == 0 else -
          1 for j in range(W+1)] for i in range(n+1)]
```

```python
def knapsack_top(arr, val, W, n):
    for i in range(1, n+1):
        for j in range(1, W+1):
            if val[i-1] <= j:
                t[i][j] = max(val[i-1] + t[i-1][j-val[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][W]  
```

# Subset Problem

Given a set of non-negative integers, and a value *sum*, determine if there is a subset of the given set with sum equal to given *sum*. 

**Example:** 

```
Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
```

```python
num = [3, 34, 4, 2, 12]
targetSum = 9
n = len(num)

t = [[True if j == 0 else False for j in range(
    targetSum+1)] for i in range(n+1)]

def subset_problem(num, targetSum, n):
    for i in range(1, n+1):
        for j in range(1, targetSum+1):
            if num[i-1] <= j:
                t[i][j] = t[i-1][j-num[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][targetSum]


print(subset_problem(num, targetSum, n))
```

# Partition problem 

Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is the same. 

**Examples:** 

```
arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.
```

```python
arr = [1, 5, 11, 5]
n = len(arr)
t = []

def subset_sum(arr, sm, n):
    for i in range(1, n+1):
        for j in range(1, sm+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][sm]

def equal_sum_partition(arr, n):
    sm = sum(arr)
    if sm % 2 != 0:
        return False
    else:
        for i in range(n+1):
            temp = []
            for j in range(sm+1):
                if j == 0:
                    temp.append(True)
                temp.append(False)
            t.append(temp)
        return subset_sum(arr, sm//2, len(arr))


print(equal_sum_partition(arr, n))
```

# Count of Subsets Sum with a Given Sum

```python
arr = [2, 3, 5, 6, 8, 10]
sm = 10

def count_of_subsets_of_given_sum(arr, sm, n):
    t = [[
        1 if j == 0 else 0 for j in range(sm+1)
    ] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, sm+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][sm]

print(count_of_subsets_of_given_sum(arr, sm, len(arr)))
```

# Partition a set into two subsets such that the difference of subset sums is minimum

Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.
**Example:** 

```
Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11        
```

```python
def subset(arr, target, n):
    t = [[
        True if j == 0 else False for j in range(target+1)
    ] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]


def minimum_subset_problem(arr):
    t = []
    s = sum(arr)
    diff = -1
    for i in range(s//2, -1, -1):
        if subset(arr, i, len(arr)):
            diff = s - (2*i)
            break
    return diff

arr = [1, 6, 11, 5]
print(minimum_subset_problem(arr))
```

# Count the number of subset with a given difference

sum(S<sub>1</sub>) - sum(S<sub>2</sub>) = diff

sum(S<sub>1</sub>) + sum(S<sub>2</sub>) = sum(arr)

=> 2 * sum(S<sub>1</sub>) = (diff + sum(arr))/2

Required count = 4 * Subset Sum Count

```python
def count_subset(arr, target, n):
    t = [[
        1 if j == 0 else 0 for j in range(target+1)
    ] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]


def count_subset_with_given_sum(arr, diff):
    return count_subset(arr, (diff+sum(arr))//2, len(arr))


arr = [1, 1, 2, 3]
print(count_subset_with_given_sum(arr, 1))
```

# Target Sum

You are given an integer array `nums` and an integer `target`.

You want to build an **expression** out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.

- For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `"+2-1"`.

Return the number of different **expressions** that you can build, which evaluates to `target`.

 

**Example 1:**

```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

**Example 2:**

```
Input: nums = [1], target = 1
Output: 1
```

```python
def count_subset(arr, target, n):
    t = [[
        1 if j == 0 else 0 for j in range(target+1)
    ] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]]+t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]


def target_sum(arr, target):
    return count_subset(arr, (target+sum(arr))//2, len(arr))


arr = [1, 1, 2, 3]
target = 1
print(target_sum(arr, target))

```


