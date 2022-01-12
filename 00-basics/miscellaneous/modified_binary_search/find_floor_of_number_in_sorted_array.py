def find_floor_of_number_in_sorted_array(arr, k):
    length = len(arr) - 1
    left, right = 0, length - 1
    floor = float("-inf")
    floor_index = -1
    if arr[0] > k:
        # floor doesn't exist in the arr
        return -1, -1
    while left <= right:
        mid = left + (right - left)//2

        if arr[mid] == k:
            return arr[mid], mid
        if arr[mid] < k:
            floor = arr[mid]
            floor_index = mid
        if arr[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return floor, floor_index


arr = [1, 2, 3, 4, 8, 10, 10, 12, 29]
print(find_floor_of_number_in_sorted_array(arr, 5))


"""
1   2   3   4   8   10  10  12  29
                ^
"""
