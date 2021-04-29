arr = [20, 17, 13, 14, 13, 12, 10, 9, 8, 4]


def search(arr, k):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + ((right-left)//2)
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            left = mid + 1
        else:
            right = mid - 1 
    return -1

print(search(arr, 4))