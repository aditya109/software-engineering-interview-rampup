def minimum_difference_element_in_sorted_array(arr, k):
    length = len(arr)
    left, right = 0, length -1 

    if arr[0] >= k:
        return arr[0]
    if arr[-1] <= k:
        return arr[-1]
    floor, ceil = -1, -1
    while left <= right:
        mid = left + (right - left)//2

        if arr[mid] == k:
            return arr[mid]
        if arr[mid] > k:
            ceil = arr[mid]
            right = mid - 1 
        else:
            floor = arr[mid]
            left = mid + 1
    floor_diff, ceil_diff = abs(floor - k), abs(ceil - k)
    if floor_diff < ceil_diff:
        return floor
    else:
        return ceil            
    

arr = [4, 6, 10]
key = 7
res = minimum_difference_element_in_sorted_array(arr, key)
print(res)