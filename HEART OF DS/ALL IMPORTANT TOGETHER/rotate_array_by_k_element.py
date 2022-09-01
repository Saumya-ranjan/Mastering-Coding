def func(arr,k):
    for i in range(k):
        arr.append(arr[0])
        arr.pop(0)
        

    print(arr)
    # for i in range(k):
    #     arr.insert(0,arr[-1])
    #     arr.pop(-1)
    # print(arr)



func([1,2,3,4,5,6,7],2)