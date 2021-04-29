def posOfFirstOne(arr):
    length = len(arr)
    left, right = 0, length - 1
    first_index = -1
    while left <= right:
        mid = left + (right-left)//2

        if arr[mid] == 1:
            first_index = mid
            right = mid - 1

        if arr[mid] < 1:
            left = mid + 1
        else:
            right = mid - 1
    return first_index


arr = [0, 0, 1, 1, 1, 1]
print(posOfFirstOne(arr))
