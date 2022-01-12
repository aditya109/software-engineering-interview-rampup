num = [3, 34, 4, 2, 12]
targetSum = 9
n = len(num)

t = [[True if j == 0 else False for j in range(
    targetSum+1)] for i in range(n+1)]

def subset_problem(num, targetSum, n):
    for i in range(n+1):
        for j in range(targetSum+1):
            if num[i-1] <= j:
                t[i][j] = t[i-1][j-num[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][targetSum]


print(subset_problem(num, targetSum, n))
