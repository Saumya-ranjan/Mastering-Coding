def func(x):
    hash = {}
    arr = []
    for i in x:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i]+=1
    for j in hash.values():
        arr.append(j)
    for k,v in hash.items():
        if v == max(arr):
            print(k)




func([2,1,3,2,3,4,5,2])