def func(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j+1 < len(arr):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)




func([67,56,76,23,12,21,345,6,5,8,9])