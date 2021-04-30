def lis(arr, n):
    t = [
        1 if i == 0 else 0 for i in range(n)
    ]

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and t[i] < t[j] + arr[i]:
                t[i] = t[j] + arr[i]
    return max(t)


arr = [1, 5, 4, 7, 12, 11]
n = len(arr)
print(lis(arr, n))
