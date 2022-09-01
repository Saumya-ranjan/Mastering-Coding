# Visualisation:
# after appending 1st row of matrix counter cloxk the number and start again:
#     |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
#     |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
#     |7 8 9|      |4 7|



def spiralOrder(matrix):
        def count_clock(matrix1):
            arr1 = []
            matrix2 = []
            count = 0
            a = len(matrix1[0])
            for i in matrix1:
                matrix2.append(i[::-1])
            while count!= a:
                arr2 = []
                for i in matrix2:
                    arr2.append(i[count])
                arr1.append(arr2)
                count+=1
            return arr1           
            
        arr = []
        arrer = [ ]
        while len(matrix)!=0:
            arr.append(matrix[0])
            matrix.pop(0)
            if len(matrix)!=0:
                matrix = count_clock(matrix)
                
        for i in range(len(arr)):
            for j in arr[i] :
                arrer.append(j)
        return arrer