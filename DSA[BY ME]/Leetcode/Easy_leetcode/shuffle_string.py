def func(x):
    str = 'codeleet'
    hash = {}
    arr = ""
    for i in range(len(str)):
        hash[x[i]] = str[i]
    for j in sorted(hash.keys()):
        arr+=hash[j]
    print(arr)
        
    


func([4,5,6,7,0,2,1,3])