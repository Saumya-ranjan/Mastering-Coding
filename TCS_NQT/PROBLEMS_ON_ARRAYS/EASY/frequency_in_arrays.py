def func(arr):
    hash = {}
    for i in arr:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i]+=1
    for i in hash.keys():
        print(i,hash[i])



func([10,5,10,15,10,5])