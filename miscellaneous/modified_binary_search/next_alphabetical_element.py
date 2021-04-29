def find_next_alphabetical_element(arr, k):
    length = len(arr)
    left, right = 0, length - 1
    next, next_index = None, -1
    if ord(arr[-1]) < ord(k):
        return -1, -1
    while left <= right:
        mid = left + (right-left)//2

        if arr[mid] == key:
            return mid
        elif ord(arr[mid]) > ord(k):
            next, next_index = arr[mid], mid

        if ord(arr[mid]) < ord(k):
            left = mid + 1
        else:
            right = mid - 1
    return next, next_index


arr = ['a', 'b', 'f', 'h']
key = 'g'
print(find_next_alphabetical_element(arr, key))
