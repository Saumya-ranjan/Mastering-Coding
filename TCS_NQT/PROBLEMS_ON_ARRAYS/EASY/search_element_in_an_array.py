def func(arr,k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1


print(func([6,7,9,5,3,10],10))