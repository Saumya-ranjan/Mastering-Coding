def func(arr):
    arr1 = []
    neg = []
    pos = []
    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    for i in range(len(arr)):
        if i < len(neg):
            arr1.append(neg[i])
        if i<len(pos):
            arr1.append(pos[i])
    print(arr1)



func([1, 2, 3, -4, -1, 4])