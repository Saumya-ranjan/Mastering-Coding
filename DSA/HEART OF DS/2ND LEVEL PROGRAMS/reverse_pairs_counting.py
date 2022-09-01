def func(arr):
    arr2 = []
    for i in range(len(arr)):
        for j in range(0,i):
            if arr[i] > 2*arr[j]:
                arr2.append([arr[i],arr[j]])
    return len(arr2)




print(func([3,2,1,4]))


