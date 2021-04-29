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
