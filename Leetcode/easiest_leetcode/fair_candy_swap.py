def func(x,y):
    arr = []
    z = int((sum(x)+sum(y))/2)
    arr.append(abs(z-sum(x)))
    arr.append(abs(z-sum(y)))
    print(arr)


func([1,2],[2,3])