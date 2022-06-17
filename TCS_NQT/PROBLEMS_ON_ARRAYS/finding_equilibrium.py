def func(arr):
    rightsum = 0
    for i in range(len(arr)):
        rightsum +=arr[i]
    leftsum  = 0 
    for i in range(len(arr)):
        rightsum -= arr[i]
        if leftsum ==rightsum:
            return i
        leftsum+=arr[i]
    return -1


print(func([2,3,-1,8,4]))