# Pattern: 0-1 Knapsack

In the 0-1 Knapsack problem, we are given a set of items, each with a weight and a value, and we need to determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

**Note**: We can either take an item or not (0-1 property). For example,

```
Input:

value = [ 20, 5, 10, 40, 15, 25 ]
weight = [ 1, 2, 3, 8, 7, 4 ]
W = 10
 
Output: Knapsack value is 60
 
value = 20 + 40 = 60
weight = 1 + 8 = 9 < W
```

The idea is to use recursion to solve this problem. For each item, there are two possibilities:

1. Include the current item in the knapsack and recur for remaining items with knapsack's decreased capacity. If the capacity becomes negative, do not recur or return `-INFINITY`.
2. Exclude the current item from the knapsack and recur for the remaining items.

Finally, return the maximum value we get by including or excluding the current item. The base case of the recursion would be when no items are left, or capacity becomes 0.

`Recursive Solution` -> `Choice Diagram`

![]()







```python

```

