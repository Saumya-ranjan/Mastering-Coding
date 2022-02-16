def func(x):
    arr =[]
    hash = {}
    for i in x:
        if i not in hash:
            hash[i] = 1
        else:
            
            hash[i] +=1
    
    for j in hash.values():
        arr.append(j)
    for k,v in hash.items():
        if v == max(arr):
            print(k)


        
        



func([3,2,3,2,2,3,3,2,2])