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
