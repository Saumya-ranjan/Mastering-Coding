# 14 5 6 2 3 6 7 8 

def func(x):
    arr = 0
    for arr in range(0,len(x)):
        for i in range(0,len(x)-1):
            if x[i]>=x[i+1]:
                x[i],x[i+1] = x[i+1],x[i]
        arr+=1
        
    print(x)



func([10,4,5,17,23,1,2])




