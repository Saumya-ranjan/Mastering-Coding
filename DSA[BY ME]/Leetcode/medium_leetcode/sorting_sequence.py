def func(s):
    kr = ""
    hash  = {}
    arr = []   
    for i in s.split(" "):
        arr.append(i)
    for j in arr:
        if j[:-1] not in hash:
            hash[j[-1]] = j[:-1]
    arr.clear()
    for k in hash.keys():
        arr.append(k)
        arr.sort()
    for i in arr:
        kr += hash[i] +" "
    kr = kr[:-1]
    print(kr)




        
        
        
            

        

        


func("is2 sentence4 This1 a3")