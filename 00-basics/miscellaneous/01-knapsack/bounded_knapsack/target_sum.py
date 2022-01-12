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
