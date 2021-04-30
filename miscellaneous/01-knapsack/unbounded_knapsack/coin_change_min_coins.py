def coin_change_min_coins(coins, target, n):
    t = [[
        0 if j == 0 else float("inf")-1 for j in range(target+1)
    ] for i in range(n+1)]

    t[0][0] = float("inf")-1
    for j in range(1, target+1):
        if j % coins[0] == 0:
            t[1][j] = j//coins[0]
        else:
            t[1][j] = float("inf")-1

    for i in range(1, n+1):
        for j in range(1, target+1):
            if coins[i-1] <= j:
                t[i][j] = min(1 + t[i][j-coins[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]


coins = [25, 10, 5]
V = 30
print(coin_change_min_coins(coins, V, len(coins)))
