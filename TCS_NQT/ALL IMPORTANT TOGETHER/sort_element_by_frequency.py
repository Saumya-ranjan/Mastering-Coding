def func(arr):
    arr1 = []
    arr2 = []
    hash = {}
    arr3 = []
    for i in arr:
        if i not in hash:
            hash[i]= 1
        else:
            hash[i]+=1
    for i in hash.values():
        if i not in arr1:
            arr1.append(i)
    arr1.sort()
    arr1 = arr1[::-1]
    for i in arr1:
        for j in sorted(hash.keys()):
            if hash[j] == i:
                arr2.append([j]*i)
    for i in arr2:
        for j in i:
            arr3.append(j)

    print(arr3)



func([1, 2, 3, 2, 4, 3, 1, 2])