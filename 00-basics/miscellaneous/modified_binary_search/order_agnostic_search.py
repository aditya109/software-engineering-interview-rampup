


def order_agnostic_search(arr, k):
    if len(arr) == 1 and arr[0] == k:
        return 1

    if len(arr) == 0:
        return -1
    isSortedReverse = True  # true if sorted in descending order

    if arr[0] < arr[1]:
        isSortedReverse = False
    left, right = 0, len(arr)-1
    while left <= right:
        mid = left + ((right - left)//2)
        if arr[mid] == k:
            return mid
        else:
            if isSortedReverse:
                if arr[mid] < k:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if arr[mid] < k:
                    left = mid + 1
                else:
                    right = mid - 1
    return -1


arr = [2, 3, 4, 10, 40]
print(order_agnostic_search(arr, 10))
arr = [20, 17, 15, 14, 13, 12, 10, 9, 8, 4]
print(order_agnostic_search(arr, 4))