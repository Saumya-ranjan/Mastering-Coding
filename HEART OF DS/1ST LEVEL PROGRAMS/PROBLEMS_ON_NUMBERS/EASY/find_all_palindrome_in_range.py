def func(min,max):
    arr = []
    for i in range(min,max):
        if str(i) == str(i)[::-1]:
            arr.append(i)
    print(arr)



func(10,50)