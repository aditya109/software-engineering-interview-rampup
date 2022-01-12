def bs_normal(arr, k):
    left, right = 0, len(arr) - 1
    length = len(arr)
    while left <= right:
        mid = left + (right-left)//2

        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def find_element_rotated_sorted_array(arr, k):
    print(arr)
    left, right = 0, len(arr) - 1
    length = len(arr)
    min_index = -1
    if arr[left] < arr[right]:
        min_index = 0
    else:
        while left <= right:
            mid = left + ((right-left)//2)

            next = (mid + 1) % length
            prev = (mid + length - 1) % length

            if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
                min_index = mid
                break
            if arr[mid] <= arr[right]:
                right = mid - 1
            elif arr[mid] >= arr[left]:
                left = mid + 1
        
    if arr[min_index] == k:
        return min_index
    else:
        left_half = arr[:min_index]
        left_index = bs_normal(left_half, k)
        if left_index == -1:
            if min_index == length -1:
                return -1
            else:
                right_half = arr[min_index+1:]
                right_index = bs_normal(right_half, k) 

                return right_index + min_index + 1
        else:
            return left_index
arr = [2, 5, 6, 8, 11, 12, 15, 18]
# arr = [11, 12, 15, 18, 2, 5, 6, 8]

# arr = [15, 18, 2, 5, 6, 8, 11, 12]
print(find_element_rotated_sorted_array(arr, 5))