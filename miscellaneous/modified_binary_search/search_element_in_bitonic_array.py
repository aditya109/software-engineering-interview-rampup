def bs(arr, k, left, right):
    length = len(arr)
    isSortedInDesc = True
    # check if it is single element
    if length == 1 and arr[0] == k:
        return 0
    if length == 1 and arr[0] != k:
        return -1

    if arr[0] < arr[1]:
        isSortedInDesc = False

    while left <= right:
        mid = left + (right-left)//2

        if arr[mid] == k:
            return mid
        else:
            if isSortedInDesc:
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


def search_element_in_bitonic_array(arr, k):
    length = len(arr)
    left, right = 0, length - 1
    peak = float("-inf")
    while left <= right:
        mid = left + (right - left)//2
        # TODO check for edges
        if arr[mid] == k:
            return mid
        if mid - 1 >= 0 and mid + 1 <= length - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                peak = mid
                break
        if arr[mid] > arr[mid - 1]:
            left = mid - 1
        else:
            right = mid + 1
    left_result = bs(arr, k, 0, peak-1)
    right_result = bs(arr, k, peak+1, length-1)
    if left_result == -1:
        if right_result == -1:
            return -1
        else:
            return right_result
    else:
        return left_result


arr = [-3, 8, 9, 20, 17, 5, 1]
key = 9
print(search_element_in_bitonic_array(arr, key))

