def func(a,b):
    arr = []
    arr1 = []
    for i in a:
        arr.append(i)
    for i in arr:
        if i not in b:
            arr1.append(i)
            
    print(arr1)


func("xyzpw","lmno")