def min_window_substring(s,t):
    hash = {}
    arr = []
    arr2 = []
    for i in range(len(s)+1):
        for j in range(i+1,len(s)+1):
            arr.append(s[i:j])
    for i in t:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] +=1
            
    for i in arr:
        hash2 = hash.copy()
        for j in i:
            if j in hash2:
                hash2[j] -=1
        count = 0
        for j in hash2.values():
            if j <=0:
                count+=1
        if count == len(set(t)):
            arr2.append(i)
    arr2.sort(key  = len)
    print(arr2[0])





min_window_substring("knkrmdvrhrgihywsoobdedhltvtmxzuhmeaakysrpybyzxq","fjknwevk")