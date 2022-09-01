def func(matrix,target):
    for i in range(len(matrix)):
        for j in matrix[i]:
            if j == target:
                return True
    return False


print(func([[1,3,5,7],[10,11,16,20],[23,30,34,60]],45))