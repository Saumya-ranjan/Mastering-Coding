def func(arr,k):
    for i in range(k):
        arr.append(arr[0])
        arr.pop(0)
        

    print(arr)


func([1,2,3,4,5,6,7],100)