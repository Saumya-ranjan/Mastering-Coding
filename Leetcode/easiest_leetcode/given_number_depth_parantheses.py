def func(x,y):
    arr1 = []
    arr = []
    count = 0
    z = x.index(y)
    for i in x[z+1:]:
        if i == '(':
            arr1.append(i)
        elif i == ')':
            arr.append(i)
    for i in range(len(arr1)):
        arr.remove(')')
    print(arr)


func("(1+(2*3)+((8)/4))(+1",'8')