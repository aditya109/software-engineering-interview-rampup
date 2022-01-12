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
