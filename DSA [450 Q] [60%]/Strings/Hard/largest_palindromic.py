def func(S):
    arr1 = []
    hash = {}
    arr2  =  []
    for i in range(len(S)+1):
        for j in range(i+1,len(S)+1):
            arr1.append(S[i:j])
    # a = (sorted(arr1,key = len))
    for i in arr1:
        if i not in hash:
            hash[i] = len(i)
    for i in hash.keys():
        if i == i[::-1]:
            arr2.append(i)
    
        
    return max(arr2,key = len)    #Main
    
        

        
    

print(func("aaaabbaa"))