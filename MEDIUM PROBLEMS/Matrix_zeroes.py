def func(matrix):
    row = []
    column = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row.append(i)
                column.append(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in row or j in column:
                matrix[i][j] = 0
    return matrix


func([[1,1,1],[1,0,1],[1,1,1]])