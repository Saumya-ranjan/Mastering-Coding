def func(arr):
    neg = []
    pos = []
    for i in arr:
        if i<0:
            neg.append(i)
        else:
            pos.append(i)
    print(neg+pos)


func([-1,56,54,2,134,45,4-3,-4,-45,-57])