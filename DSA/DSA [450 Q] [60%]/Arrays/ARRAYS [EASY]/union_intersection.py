def func(a,b):
    arr = []
    for i in a:
        if i in b:
            arr.append(i)   # Intersection
    c = a+b
    for i in arr:
        c.remove(i)
    print(c)      #Union

    print(arr)




func([1,2,3],[1,2,3,4,5])