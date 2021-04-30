
def knapsack_r(arr, val, W, n):
    if n == 0 or W == 0:
        return 0

    if arr[n-1] <= W:
        return max(val[n-1] + knapsack_r(arr, val, W-val[n-1], n-1), knapsack_r(arr, val, W, n-1))
    else:
        return knapsack_r(arr, val, W, n-1)


t = [[0 if i == 0 or j == 0 else -
      1 for j in range(W+1)] for i in range(n+1)]


def knapsack_m(arr, val, W, n):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    if arr[n-1] <= W:
        t[n][W] = max(val[n-1] + knapsack_m(arr, val, W-val[n-1],
                                            n-1), knapsack_m(arr, val, W, n-1))
        return t[n][W]
    else:
        t[n][W] = knapsack_m(arr, val, W, n-1)
        return t[n][W]


def knapsack_top(arr, val, W, n):
    for i in range(n+1):
        for j in range(W+1):
            if val[i-1] <= j:
                t[i][j] = max(val[i-1] + t[i-1][j-val[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][W]

wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]

W = 7
n = 4


print(knapsack_top(wt, val, W, n)) # 7