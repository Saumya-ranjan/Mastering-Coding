def func(x):             #Normal way to solve this
    arr = []
    par = []
    for i in range(0,len(x)):
        if x[i] != 0:
            arr.append(x[i])
        else:
            par.append(x[i])
    print(arr+par)
        
func([1,0,3,4,5,0,2,3,0])

