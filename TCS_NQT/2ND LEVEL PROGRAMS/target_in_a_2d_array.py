def func(arr,target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return True
    return False


print(func([[1,3,5,7],[10,11,16,20],[23,30,34,60]],61))