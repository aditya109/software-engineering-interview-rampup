arr = [1, 5, 11, 5]
n = len(arr)
t = []


def subset_sum(arr, sm, n):
    for i in range(n+1):
        for j in range(sm+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][sm]

def equal_sum_partition(arr, n):
    sm = sum(arr)
    if sm % 2 != 0:
        return False
    else:
        for i in range(n+1):
            temp = []
            for j in range(sm+1):
                if j == 0:
                    temp.append(True)
                temp.append(False)
            t.append(temp)
        return subset_sum(arr, sm//2, len(arr))


print(equal_sum_partition(arr, n))
