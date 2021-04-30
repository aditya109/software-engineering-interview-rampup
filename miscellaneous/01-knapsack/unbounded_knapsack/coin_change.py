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
