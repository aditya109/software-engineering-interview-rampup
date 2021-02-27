# Floyd-Warshall Algorithm
'''
4 4
0 3 10 
0 1 5 
1 2 3 
2 3 1


'''
INF = float('inf')


def printmaxtrix(m):
    r, c = len(m), len(m[0])
    for i in range(r):
        for j in range(c):
            print(m[i][j], end=" ")
        print()


v, e = map(int, input().split())
m = [[None] * v for i in range(v)]
for i in range(v):
    for j in range(v):
        # src and dest are same
        if i == j:
            m[i][j] = 0
        # else doesn't exist
        else:
            m[i][j] = INF

# take input values

for i in range(e):
    src, dest, wt = map(int, input().split())
    m[src][dest] = wt

print("-----------------------")
printmaxtrix(m)


# apply our FWA
# Time Complexity = O(v^3)
for k in range(v):
    for i in range(v):
        for j in range(v):
            # cost of temporary path is less
            # update
            if m[i][k] + m[k][j] < m[i][j]:
                m[i][j] = m[i][k] + m[k][j]
print("-----------------------")
printmaxtrix(m)
