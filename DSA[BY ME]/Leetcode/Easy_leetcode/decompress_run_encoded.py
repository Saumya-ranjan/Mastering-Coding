def func(x):          #o(n^2)
    value=[]
    freq = []
    res = []
    
    for i in range(len(x)):
        if i %2==0:
            freq.append(x[i])
        else:
            value.append(x[i])
    
    for j in range(len(freq)):
        for k in range(freq[j]):
            res.append(value[j])
            

    print(res)


        
    

func([1,2,3,4])