def func(x):
    arr = [0]
    value = 0
    for i in range(len(x)):
        value+= x[i]
        arr.append(value)
    print(max(arr))




func([-5,1,5,0,-7])