#interview bit    #Not done

def func(x):
    arr = []
    for i in range(len(x)):
        arr.append(1)
    for i in range(1,len(x)):
        if x[i]>x[i-1]:
            arr[i] = arr[i-1]+1
    print(arr)

        
        
        


func([1,3,2,1])