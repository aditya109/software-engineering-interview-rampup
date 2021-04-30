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
