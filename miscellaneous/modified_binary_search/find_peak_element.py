def find_peak_element(arr):
    length = len(arr)
    left, right = 0, length - 1

    while left <= right:
        mid = left + (right - left) // 2
        if mid == 0 and mid + 1 <= length - 1:
            if arr[mid] > arr[mid + 1]:
                return arr[mid]
        if mid == length - 1 and mid - 1 >= 0:
            if arr[mid] > arr[mid - 1]:
                return arr[mid]

        if mid > 0 and mid < length - 1:
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid - 1]:
                return mid
        if arr[mid] > arr[mid-1]:
            # go right
            left = mid + 1
        else:
            # go left
            right = mid - 1


arr = [1, 2, 1, 3, 5, 6, 4]
print(find_peak_element(arr))
