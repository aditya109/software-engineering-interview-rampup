# Unbounded Knapsack

Multiple occurrence are allowed.

Given a knapsack weight **W** and a set of **n** items with certain value *vali* and weight *wti*, we need to calculate the maximum amount that could make up this quantity exactly. This is different from [classical Knapsack problem](https://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/), here we are allowed to use unlimited number of instances of an item.
**Examples:** 

```
Input : W = 100
       val[]  = {1, 30}
       wt[] = {1, 50}
Output : 100
There are many ways to fill knapsack.
1) 2 instances of 50 unit weight item.
2) 100 instances of 1 unit weight item.
3) 1 instance of 50 unit weight item and 50
   instances of 1 unit weight items.
We get maximum value with option 2.

Input : W = 8
       val[] = {10, 40, 50, 70}
       wt[]  = {1, 3, 4, 5}       
Output : 110 
We get maximum value with one unit of
weight 5 and one unit of weight 3.
```

```python
def unbounded_knapsack(wt, val, W, n):
    t = [[
        0 for j in range(W+1)
    ] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= W:
                t[i][j] = max(val[i-1] + t[i][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][W]


wt = [1, 50]
val = [1, 30]

W = 100
n = 2
print(unbounded_knapsack(wt, val, W, n))
```

# Cutting a Rod

Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

```
length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
```

And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1) 

```
length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
```

```python
def get_cut_pieces(length, price, target, n):
    t = [[
        0 for j in range(target+1)
    ] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, target+1):
            if length[i-1] <= j:
                t[i][j] = max(price[i-1] + t[i][j-length[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]


length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
target = 8

print(get_cut_pieces(length, price, target, len(length)))
```

# Coin Change 

Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.

```python
def count_subsets(coins, target, n):
    t = [[
        1 if j == 0 else 0 for j in range(target+1)
    ] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, target+1):
            if coins[i-1] <= j:
                t[i][j] = t[i][j-coins[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    return t[n][target]


def coin_change(coins, target):
    return count_subsets(coins, target, len(coins))


arr = [1, 2, 3]
target = 4
print(coin_change(arr, target))
```

# Coin change problem: Minimum number of coins

Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change? If it’s not possible to make change, print -1.

**Examples:** 

```
Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents 

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents
```

```python
def coin_change_min_coins(coins, target, n):
    t = [[
        0 if j == 0 else float("inf")-1 for j in range(target+1)
    ] for i in range(n+1)]

    # important
    t[0][0] = float("inf")-1
    for j in range(1, target+1):
        if j % coins[0] == 0:
            t[1][j] = j//coins[0]
        else:
            t[1][j] = float("inf")-1

    for i in range(1, n+1):
        for j in range(1, target+1):
            if coins[i-1] <= j:
                 # important
                t[i][j] = min(1 + t[i][j-coins[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]


coins = [25, 10, 5]
V = 30
print(coin_change_min_coins(coins, V, len(coins)))

```


