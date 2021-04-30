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