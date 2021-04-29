def isValid(books, m, maximum):
    s1 = 1
    s = 0
    for i in range(len(books)):
        s += books[i]
        if s > maximum:
            s1 += 1
            s = books[i]
            if s1 > m:
                return False
    return True

def allocate_minimum_number_of_pages(books, m):
    left = max(books)
    right = sum(books)
    if len(books) < m:
        return -1
    res = -1
    while left <= right:
        mid = left + (right-left)//2

        if isValid(books, m, mid):
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

arr = [12, 34, 67, 90]
m = 2
print(allocate_minimum_number_of_pages(books=arr, m=m))