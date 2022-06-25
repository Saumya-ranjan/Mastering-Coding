def func(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if j <= len(arr):
                if arr[i] > arr[j]:
                    count+=1
    return count


print(func([1,2,3,4,5]))