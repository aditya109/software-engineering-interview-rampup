def find_rotation_count(arr):
    """
    case 1: min element is in between 0 and len(arr) - 1
    case 2: min element is at 0
    case 3: min element is at len(arr) -1
    """
    left, right = 0, len(arr) - 1
    length = len(arr)
    if arr[left] < arr[right]:
        return 0
    
    while left <= right:
        mid = left + ((right-left)//2) # 3
        next = (mid + 1) % length   # 4
        prev = (mid + length - 1) % length # 2
        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid
            """
            if arr[left] < arr[mid]
                left array is sorted
            if arr[mid] > arr[right]
                right array is sorted
            """
        if arr[mid] <= arr[right]:
            right = mid -1 
        elif arr[mid] >= arr[left]:
            left = mid + 1

arr = [2, 5, 6, 8, 11, 12, 15, 18]
arr = [11, 12, 15, 18, 2, 5, 6, 8]

# arr = [15, 18, 2, 5, 6, 8, 11, 12]
print(find_rotation_count(arr))
