# Searching in Descending Sorted Array

```python
arr = [20, 17, 13, 14, 13, 12, 10, 9, 8, 4]


def search(arr, k):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + ((right-left)//2)
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            left = mid + 1
        else:
            right = mid - 1 
    return -1

print(search(arr, 4))
```

# Order Agnostic Search

```python
def order_agnostic_search(arr, k):
    if len(arr) == 1 and arr[0] == k:
        return 1

    if len(arr) == 0:
        return -1
    isSortedReverse = True  # true if sorted in descending order

    if arr[0] < arr[1]:
        isSortedReverse = False
    left, right = 0, len(arr)-1
    while left <= right:
        mid = left + ((right - left)//2)
        if arr[mid] == k:
            return mid
        else:
            if isSortedReverse:
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


arr = [2, 3, 4, 10, 40]
print(order_agnostic_search(arr, 10))
arr = [20, 17, 15, 14, 13, 12, 10, 9, 8, 4]
print(order_agnostic_search(arr, 4))
```

# First and Last Occurrence of an Element

```python
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
```

# Count Elements in Sorted Array

```python
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
```

# Find Rotation Count of sorted Rotated Array  

```python
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
```

# Find Element in sorted rotated array

```python
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
```

# Searching in a Nearly Sorted Array

Given an array which is sorted, but after sorting some elements are moved to either of the adjacent positions, i.e., `arr[i]` may be present at `arr[i+1]` or `arr[i-1]`. Write an efficient function to search an element in this array. Basically the element `arr[i]` can only be swapped with either `arr[i+1]` or `arr[i-1]`.

For example consider the array `{2, 3, 10, 4, 40}`, 4 is moved to next position and 10 is moved to previous position.

**Example :**

```
Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
Output: 2 
Output is index of 40 in given array

Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 90
Output: -1
-1 is returned to indicate element is not present
```

```python
def search_in_nearly_sorted_array(arr, k):
    length = len(arr)
    left, right = 0, length - 1

    while left <= right:
        mid = left + (right-left)//2

        if arr[mid] == k:
            return mid
        elif mid + 1 <= right and arr[mid + 1] == k:
            return mid + 1
        elif mid - 1 >= left and arr[mid - 1] == k:
            return mid - 1
        if arr[mid] > k:
            right = mid - 2
        else:
            left = mid + 2
    return -1

arr = [2, 5, 6, 8, 12, 11, 15, 18]

print(search_in_nearly_sorted_array(arr, 5))
```

# Find Floor of an element in a Sorted Array

Given a sorted array and a value x, the floor of x is the largest element in array smaller than or equal to x. Write efficient functions to find floor of x.
**Examples:** 

```
Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 5
Output : 2
2 is the largest element in 
arr[] smaller than 5.

Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 20
Output : 19
19 is the largest element in
arr[] smaller than 20.

Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 0
Output : -1
Since floor doesn't exist,
output is -1.
```

```python
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
```

# Find Ceil of an element in a Sorted Array

Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x, and the floor is the greatest element smaller than or equal to x. Assume than the array is sorted in non-decreasing order. Write efficient functions to find floor and ceiling of x. 
**Examples :** 
 

```
For example, let the input array be {1, 2, 8, 10, 10, 12, 19}
For x = 0:    floor doesn't exist in array,  ceil  = 1
For x = 1:    floor  = 1,  ceil  = 1
For x = 5:    floor  = 2,  ceil  = 8
For x = 20:   floor  = 19,  ceil doesn't exist in array
```

```python
def find_ceil_of_number_in_sorted_array(arr, k):
    length = len(arr)-1
    left, right = 0, length - 1

    ceil, ceil_index = float("-inf"), -1
    if arr[-1] < k:
        return -1, -1
    while left <= right:
        mid = left + ((right-left)//2)

        if arr[mid] == k:
            return arr[mid], mid
        elif arr[mid] > k:
            ceil, ceil_index = arr[mid], mid

        if arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return ceil, ceil_index


arr = [1, 2, 3, 4, 8, 10, 10, 12, 29]
print(find_ceil_of_number_in_sorted_array(arr, 5))
```

# Next Alphabetical Element

Given an array of letters sorted in ascending order, find the smallest letter in the array which is greater than a given key letter. 

```python
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
```

# Find position of an element in an Infinite Sorted Array

Suppose you have a sorted array of infinite numbers, how would you search an element in the array?

```python
we can do a normal BS in finite array
def normal_BS(arr, left, right, k)-> mid:
    pass

def filter_infinite_array(arr, k):
    SIZE = 10000
    left = 0
   	right = SIZE
    while True:
        if k <= arr[right]:
            # we found the array
            return normal_BS(arr, left, right, k
        else:
            right += SIZE
            left += right + 1            
```

# Index of First 1 in a Binary Sorted Infinite Array

Given an infinite sorted array consisting 0s and 1s. The problem is to find the index of first ‘1’ in that array. As the array is infinite, therefore it is guaranteed that number ‘1’ will be present in the array.

**Examples:**

```
Input : arr[] = {0, 0, 1, 1, 1, 1} 
Output : 2

Input : arr[] = {1, 1, 1, 1, 1, 1, 1}
Output : 0
```

```python
def posOfFirstOne(arr):
    length = len(arr)
    left, right = 0, length - 1
    first_index = -1
    while left <= right:
        mid = left + (right-left)//2

        if arr[mid] == 1:
            first_index = mid
            right = mid - 1

        if arr[mid] < 1:
            left = mid + 1
        else:
            right = mid - 1
    return first_index


arr = [0, 0, 1, 1, 1, 1]
print(posOfFirstOne(arr))
```

# Minimum Difference Element in a Sorted Array

Given a sorted array, find the element in the array which has minimum difference with the given number.  

```python
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
```

# Binary Search on Answer

Binary Search applied on unsorted  

# Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given an integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

**Example 2:**

```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

**Example 3:**

```
Input: nums = [1,2,3]
Output: 3
Explanation: 3 is a peak element and your function should return the index number 2.
```

```python
def find_peak_element(arr):
    length = len(arr)
    left, right = 0, length - 1
	
    while left <= right:
        mid = left + (right - left) // 2
        if mid  == 0:
            
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
```

# Find max element in a Bitonic Array

**Given a bitonic array find the maximum value of the array**. An array is said to be **bitonic** if it has an increasing sequence of integers followed immediately by a decreasing sequence of integers.

**Example:**

```
Input:
1 4 8 3 2

Output:
8
```

```python
def find_max_element_bitonic_array(arr):
    length = len(arr)

    left, right = 0, length - 1

    while left <= right:
        mid = left + (right-left)//2
        if mid == 0 and mid + 1 <= length - 1:
            if arr[mid] > arr[mid + 1]:
                return arr[mid]
        if mid == length - 1 and mid - 1 >= 0:
            if arr[mid] > arr[mid - 1]:
                return arr[mid]
        if mid - 1 >= 0 and mid + 1 <= length - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
        if arr[mid] > arr[mid - 1]:
            # go right
            left = mid + 1
        else:
            # go left
            right = mid - 1
    return -1


arr = [1, 3, 4, 8, 12, 4, 2]
print(find_max_element_bitonic_array(arr))
```

# Search An Element in Bitonic Array 

Given a bitonic sequence of n distinct elements, write a program to find a given element x in the bitonic sequence in O(log n) time. A Bitonic Sequence is a sequence of numbers that is first strictly increasing then after a point strictly decreasing.

**Examples:** 

```
Input :  arr[] = {-3, 9, 18, 20, 17, 5, 1};
         key = 20
Output : Found at index 3

Input :  arr[] = {5, 6, 7, 8, 9, 10, 3, 2, 1};
         key = 30
Output : Not Found
```

```python
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
```

# Search in a row wise and column wise sorted matrix

Given an n x n matrix and a number x, find the position of x in the matrix if it is present in it. Otherwise, print “Not Found”. In the given matrix, every row and column is sorted in increasing order. The designed algorithm should have linear time complexity. 

1. Let the given element be x, create two variable *i = 0, j = n-1* as index of row and column
2. Run a loop until i = 0
3. Check if the current element is greater than x then decrease the count of j. Exclude the current column.
4. Check if the current element is less than x then increase the count of i. Exclude the current row.
5. If the element is equal then print the position and end.

**Example:** 

```
Input: mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 29
Output: Found at (2, 1)
Explanation: Element at (2,1) is 29

Input : mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 100
Output : Element not found
Explanation: Element 100 is not found
```

```python
def search(mat, row, key):
    i, j = 0, row-1
    while i < row and j >= 0:
        if mat[i][j] == key:
            return i, j
        if mat[i][j] > key:
            j -= 1
        else:
            i += 1
    return -1, -1


mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]
print(search(mat, 4, 29))
```

# Allocate Minimum Number Of Pages

Given number of pages in n different books and m students. The books are arranged in ascending order of number of pages. Every student is assigned to read some consecutive books. The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum.

**Example :**

```
Input : pages[] = {12, 34, 67, 90}
        m = 2
Output : 113
Explanation:
There are 2 number of students. Books can be distributed 
in following fashion : 
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student 
      2 with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student
      2 with 67 + 90 = 157 pages 
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student 
      1 with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113. 
```

```python
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
```

