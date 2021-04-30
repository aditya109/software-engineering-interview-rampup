n = [-1, 3, 4, 5, 2, 2, 2, 2]


def lis(arr, n):
    t = [1 if i == 0 else 0 for i in range(n)]
    for i in range(1, n):
        t[i] = 1
        for j in range(0, i):
            if arr[i] > arr[j] and t[i] < t[j] + 1:
                t[i] = t[j] + 1
    return max(t)

print(lis(n, len(n)))