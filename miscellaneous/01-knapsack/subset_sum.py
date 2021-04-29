wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]

W = 7
n = 4

"""
W = 0
n = 0
==> Base case

if wt[n-1] <= W
    return max(v[n-1] + knapsack(wt, val, W-wt[n-1], n-1),knapsack(wt, val, W, n-1))
else if wt[n-1] > W
    return knapsack(wt, val, W, n-1)
"""
