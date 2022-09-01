def func(arr):
    rows = []
    columns = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                rows.append(i)
                columns.append(j)
    for i in rows:
        for j in range(len(arr)):
            arr[i][j] = 0
    for i in range(len(arr)):
        for j in columns:
            arr[i][j] = 0
    print(arr)
                
                
func([[0,1,2,0],[3,4,5,2],[1,3,1,5]])


#  1    1    1
#  1    0    1
#  1    1    1