def func(matrix,k):
    arr1 = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            arr1.append(matrix[i][j])
    arr1.sort()
    for i in range(len(arr1)):
        if i == k-1:
            return arr1[i]



print(func( [[16, 28, 60, 64],
        [22, 41, 63, 91],
        [27, 50, 87, 93],
        [36, 78, 87, 94 ]],3))