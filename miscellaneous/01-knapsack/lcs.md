# Longest Common Subsequence

## Recursive

*LCS Problem Statement:* Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 

```
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.
```

```python
def lcs_r(x, y, n, m):
    if n == 0 or m ==0:
        return 0
    if x[n-1] == y[m-1]:
        return 1 + lcs_r(x, y, n-1, m-1)
    else:
        return max(lcs_r(x, y, n-1, m), lcs_r(x, y, n, m-1))

x = "ABCDGH"
y = "AEDFHR"

print(lcs_r(x, y, len(x), len(y)))
```

## Memoization

```python
def lcs_m(x, y, n, m):
    if n == 0 or m == 0:
        return 0

    if t[m][n] != -1:
        return t[m][n]
    if x[n-1] == y[m-1]:
        t[m][n] = 1 + lcs_m(x, y, n-1, m-1)
        return t[m][n]
    else:
        t[m][n] = max(lcs_m(x, y, n, m-1), lcs_m(x, y, n-1, m))
        return t[m][n]

x = "ABCDGH"
y = "AEDFHR"
n = len(x)
m = len(y)
t = [[
    -1 for j in range(n+1)
] for i in range(m+1)]

print(lcs_m(x, y, len(x), len(y)))
```

## Top-Down Approach

```python
x = "ABCDGH"
y = "AEDFHR"
n = len(x)
m = len(y)
t = [[
    -1 for j in range(n+1)
] for i in range(m+1)]


def lcs_top(x, y, n, m):
    t = [[
        0 for i in range(n+1)
    ] for j in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif x[j-1] == y[i-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t[m][n]


print(lcs_top(x, y, len(x), len(y)))
```

# Longest Common Substring

Given two strings ‘X’ and ‘Y’, find the length of the longest common substring. 

```
Examples : 

Input : X = “GeeksforGeeks”, y = “GeeksQuiz” 
Output : 5 
Explanation:
The longest common substring is “Geeks” and is of length 5.

Input : X = “abcdxyz”, y = “xyzabcd” 
Output : 4 
Explanation:
The longest common substring is “abcd” and is of length 4.

Input : X = “zxabcdezy”, y = “yzabcdezx” 
Output : 6 
Explanation:
The longest common substring is “abcdez” and is of length 6.
```



```python
def longest_common_substring(x, y, n, m):
    t = [[
        0 for j in range(n+1)
    ] for i in range(m+1)]
    result = 0
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif x[j-1] == y[i-1]:
                t[i][j] = 1 + t[i-1][j-1]
                result = max(result, t[i][j])
            else:
                t[i][j] = 0
    return result


x = 'OldSite:GeeksforGeeks.org'
y = 'NewSite:GeeksQuiz.com'
n = len(x)
m = len(y)

print(longest_common_substring(x, y, n, m))
```

# Print Longest Common Subsequence

```python

```



```python

```



```python

```



```python

```



```python

```

