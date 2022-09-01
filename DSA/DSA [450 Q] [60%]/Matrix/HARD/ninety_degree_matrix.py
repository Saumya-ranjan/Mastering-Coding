def func(matrix):
    arr1 = []
    arr2 = []
    for i in range(len(matrix)) :
        for j in range(len(matrix) - 1, -1, -1) :
            arr1.append(matrix[j][i])
    print(arr1)
            
    j = 0
    for i in range(1,len(arr1)+1):      
        if i%len(matrix) == 0:
            arr2.append(arr1[j:i])
            j=i
            
    print(arr2)



            

func([[1 ,2 ,3], 
[4, 5, 6],
[7, 8, 9 ]])