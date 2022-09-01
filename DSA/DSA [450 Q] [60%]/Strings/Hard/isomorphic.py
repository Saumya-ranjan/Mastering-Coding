def func(str1,str2):
    hash = {}
    hash1 = {}
    for i in range(len(str1)):
        if str1[i] not in hash:
            hash[str1[i]] =[i]  
        else:
            hash[str1[i]]+=[i]
    for i in range(len(str2)):
        if str2[i] not in hash1:
            hash1[str2[i]] =[i]  
        else:
            hash1[str2[i]]+=[i]
    if sorted(hash.values()) == sorted(hash1.values()):
        return 1
    return 0
print(func( 'abb','xyy'))