#N X N MATRIX

def func(matrix):
    arr1 = []
    arr2 = []
    for i in matrix:
        value = len(i)
        for j in range(len(i)):            
            arr1.append(i[j])
    arr1.sort()
    for i in range(len(arr1)+1):
        if i ==0:
            continue
        elif i%value == 0:
            j = i-value
            arr2.append(arr1[j:i])
    print(arr2)
        

    

func([[1,2,3],[4,5,6],[7,8,9]])