def func(arr):
    arr1 = []
    hash = {}
    arr2 = []
    for i in set(arr):
        arr1.append(i)
    arr1.sort()
    for i in arr1:
        if i not in hash:
            hash[i] = arr1.index(i)+1
    for i in arr:
        arr2.append(hash[i])
    print(arr2)


    





func([1 ,5 ,8 ,15 ,8 ,25 ,9])