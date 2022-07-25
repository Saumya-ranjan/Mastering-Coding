def falling_path(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i ==0:
                matrix[i][j] = matrix[i][j]
            elif j==0 and i > 0:
                matrix[i][j] = min(matrix[i-1][j]+ matrix[i][j], matrix[i-1][j+1]+matrix[i][j])
            elif j == len(matrix[0])-1 and i>0:
                matrix[i][j] = min(matrix[i-1][j] +matrix[i][j], matrix[i-1][j-1]+matrix[i][j])
            else:
                matrix[i][j] = min(matrix[i-1][j]+matrix[i][j] , matrix[i-1][j-1] +matrix[i][j], matrix[i-1][j+1]+matrix[i][j])
    return min(matrix[-1])


falling_path([[2,1,3],[6,5,4],[7,8,9]])