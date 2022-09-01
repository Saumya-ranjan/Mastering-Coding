# 2 BY 2 MATRIX IS USED IN THIS CASE:
def func(x):
    row = []
    column = []
    for i in x:
        row.append(max(i))
    for j in zip(*x):
        column.append((max(j)))
    print(row,column)

    
    



func([[1,2,3,4],[2,3,7,8],[3,5,67,78],[4,2,5,6]])