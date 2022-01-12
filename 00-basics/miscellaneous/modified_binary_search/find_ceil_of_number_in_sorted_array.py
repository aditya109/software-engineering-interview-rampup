def find_ceil_of_number_in_sorted_array(arr, k):
    length = len(arr)-1
    left, right = 0, length - 1

    ceil, ceil_index = float("-inf"), -1
    if arr[-1] < k:
        return -1, -1
    while left <= right:
        mid = left + ((right-left)//2)

        if arr[mid] == k:
            return arr[mid], mid
        elif arr[mid] > k:
            ceil, ceil_index = arr[mid], mid

        if arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return ceil, ceil_index


arr = [1, 2, 3, 4, 8, 10, 10, 12, 29]
print(find_ceil_of_number_in_sorted_array(arr, 5))
