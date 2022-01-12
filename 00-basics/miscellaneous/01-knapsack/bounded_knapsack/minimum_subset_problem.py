def subset(arr, target, n):
    t = [[
        True if j == 0 else False for j in range(target+1)
    ] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]


def minimum_subset_problem(arr):
    t = []
    s = sum(arr)
    diff = -1
    for i in range(s//2, -1, -1):
        if subset(arr, i, len(arr)):
            diff = s - (2*i)
            break
    return diff



arr = [3, 1, 4, 2, 2, 1]
print(minimum_subset_problem(arr))
