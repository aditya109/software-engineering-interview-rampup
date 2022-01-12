def lcs_r(x, y, n, m):
    if n == 0 or m == 0:
        return 0
    if x[n-1] == y[m-1]:
        return 1 + lcs_r(x, y, n-1, m-1)
    else:
        return max(lcs_r(x, y, n-1, m), lcs_r(x, y, n, m-1))


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
