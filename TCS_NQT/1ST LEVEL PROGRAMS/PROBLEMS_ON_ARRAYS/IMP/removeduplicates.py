def func(arr):
    arr1 = []
    hash = {}
    for i in arr:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i]+=1
    for k in hash.keys():
        arr1.append(k)
    for i in range(len(arr)-len(arr1)):
        arr1.append('_')
    print(arr1)



func([1,1,1,2,2,3,3,3,3,4,4])