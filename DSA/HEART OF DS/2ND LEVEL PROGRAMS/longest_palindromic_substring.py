# -- >  Bruteforce Method

def func(str1):
    arr = []
    arr1 = []
    hash = {}
    for i in range(len(str1)+1):
        for j in range(i+1,len(str1)+1):
            arr.append(str1[i:j])
    for i in arr:
        if i == i[::-1]:
            arr1.append(i)
    arr1.sort(key = len)
    for i in arr1:
        if len(i) not in hash:
            hash[len(i)] = i
    a = max(hash.keys())
    return hash[a]
    

print(func("aeioc"))