def func(n):
    hash1 = {}
    value = 0
    hash = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    arr = ['I','V','X','L','C','D','M'] 
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            hash1[arr[i]+arr[j]] = hash[arr[j]] - hash[arr[i]]
    for i in hash1.keys():
        if i in n:
            n = n.replace(i,"")
            value+=hash1[i]
    for i in n:
        if i in hash.keys():
            value+=hash[i]
    print(value)



        

func('MCMXCIV')