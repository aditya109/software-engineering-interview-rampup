def find_first_occurrence(arr, k):
    left, right = 0, len(arr)-1
    first_occurence = float("inf")
    while left <= right:
        mid = left + ((right-left)//2)

        if arr[mid] == k:
            first_occurence = min(first_occurence, mid)
            right = mid - 1
        elif arr[mid] > k:
            left = mid + 1
        else:
            right = mid - 1
    if first_occurence != float("inf"):
        return first_occurence
    return -1


def find_last_occurrence(arr, k):
    left, right = 0, len(arr)-1
    last_occurence = float("-inf")
    while left <= right:
        mid = left + ((right-left)//2)

        if arr[mid] == k:
            last_occurence = max(last_occurence, mid)
            left = mid + 1
        elif arr[mid] > k:
            left = mid + 1
        else:
            right = mid - 1
    if last_occurence != float("inf"):
        return last_occurence
    return -1


def count_element_in_sorted_array(arr, k):
    first_index = find_first_occurrence(arr, k)
    last_index = find_last_occurrence(arr, k)
    if first_index == -1 and last_index == -1:
        return 0
    elif first_index == last_index:
        return 1
    else:
        return last_index - first_index + 1


arr = [2, 4, 5, 10, 10, 10, 18, 20]
print(count_element_in_sorted_array(arr, 10))
