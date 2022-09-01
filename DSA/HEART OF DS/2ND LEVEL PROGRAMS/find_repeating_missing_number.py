def func(arr):
    hash = {}
    res  = []
    for i in arr:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i]+=1
    for i in hash.keys():
        if hash[i] > 1:
            res.append(i)
    for i in range(1,len(arr)+1):
        if i not in arr:
            res.append(i)
    return res
        



print(func([3,1,2,5,3]))