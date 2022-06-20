def func(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    print(arr)

func([34,345,6,23,567,89,4,3,89,6,54,12,1])