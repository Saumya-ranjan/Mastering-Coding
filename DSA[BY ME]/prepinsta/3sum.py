def func(x): 
    arr1 = []
    x.sort()
    if len(x)<3:
        print(0)
    else:
        arr = []               #Brute Force Method
        for i in range(len(x)):
            for j in range(i+1,len(x)):
                for k in range(j+1,len(x)):
                    if i!=j and i!=k and j!=k and x[i] + x[j] + x[k] == 0 :
                        arr.append([x[i],x[j],x[k]])
        
        for i in arr:
            if i not in arr1:
                arr1.append(i)
        print(arr1)

            
        
        
func( [0,0,0,0])