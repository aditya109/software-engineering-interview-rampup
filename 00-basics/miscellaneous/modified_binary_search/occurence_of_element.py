def first_occurrence_element(arr, k):
    left, right = 0, len(arr)-1
    first_index = float("inf")
    while left <= right:
        mid = left + ((right-left)//2)

        if arr[mid] == k:
            first_index = mid
            right = mid - 1
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    if first_index != float("inf"):
        return first_index
    return -1

def last_occurrence_element(arr, k):
    left, right = 0, len(arr)-1
    last_index = float("-inf")
    while left <= right:
        mid = left + ((right-left)//2)

        if arr[mid] == k:
            last_index = max(last_index, mid)
            left = mid + 1
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    if last_index != float("-inf"):
        return last_index
    return -1

arr = [2, 4, 5, 10, 10, 10, 18, 20]
print(first_occurrence_element(arr, 10))
print(last_occurrence_element(arr, 10))