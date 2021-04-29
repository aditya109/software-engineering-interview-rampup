def search_in_nearly_sorted_array(arr, k):
    length = len(arr)
    left, right = 0, length - 1

    while left <= right:
        mid = left + (right-left)//2

        if arr[mid] == k:
            return mid
        elif mid + 1 <= right and arr[mid + 1] == k:
            return mid + 1
        elif mid - 1 >= left and arr[mid - 1] == k:
            return mid - 1
        if arr[mid] > k:
            right = mid - 2
        else:
            left = mid + 2
    return -1

arr = [2, 5, 6, 8, 12, 11, 15, 18]

print(search_in_nearly_sorted_array(arr, 5))
