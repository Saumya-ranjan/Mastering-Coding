def func(arr,arr1):
    count = 0
    for i in arr:
        if i in arr1:
            count+=1
    if count == len(arr):
        return 1
    return -1

print(func( [1,3,4,5,2],[4,5,2]))
