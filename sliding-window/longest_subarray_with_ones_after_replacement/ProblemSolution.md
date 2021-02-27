# Longest Subarray of 1s after replacement

Given an array `A` of 0s and 1s, we may change up to `K` values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

**Example 1:**

```
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
```

**Example 2:**

```
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
```

## Solution:

**Pseudocode:** **O(k*n)**

```pseudocode
function find_consecutive_ones(arr, k):
    arrLength := length(arr)
    unaryCounts := [0, 0]
    
    windowStart := 0
    maximumLength := 0
    maximumCount := 0
    
    for every index in range(arrLength)
    	unaryCounts[A[index]] += 1
        countOfOnes := unaryCounts[A[1]]
        maxCount = max(maximumCount, countOfOnes)
    	
        while windowStart <= windowEnd and unaryCounts[0] > k
        	unaryCounts[arr[windowStart]] -= 1
            windowStart += 1
        maximumLength = max(maximumLength, windowEnd - windowStart + 1)
    endfor
    return maximumLength

endfunction
```

**Pseudocode:** **O(n)**

```pseudocode
function find_consecutive_ones(arr, k):
    windowStart := 0
    arrLength := length(arr)
        
    for every windowEnd in range(arrLength)
    	k -= 1 - arr[windowEnd]
    	if k < 0:
    		k += 1 - arr[windowStart]
    		windowStart += 1
    endfor
    return windowEnd - windowStart + 1

endfunction
```

