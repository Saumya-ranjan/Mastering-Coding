def func(matrix,arr3):
    arr = []
    arr1 = []
    start= matrix[0]
    end = []
    matrix.remove(start)
    if len(matrix)!=0:
        end = matrix[-1]
        matrix.remove(end)
    if len(matrix)!=0:
        for i in matrix:
            arr.append(i[-1])
            i.remove(i[-1])
            arr1.append(i[0])
            i.remove(i[0])
    arr3+=(start+arr)
    if len(end)!=0:
        arr3.append(end[::-1])
    arr3.append(arr1[::-1])
    
    
    if len(matrix)!=0:
        func(matrix,arr3) 
    return arr3
print(func([[1, 2, 3, 4],[5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15,16],[17,18,19,20]],[]))