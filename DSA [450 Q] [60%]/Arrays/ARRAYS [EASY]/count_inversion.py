def func(arr):
    arr1 = []
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j] and i<j:
                arr1.append([arr[i],arr[j]])
    for i in arr1:
        count+=1
    return count



print(func([2, 4, 1, 3, 5]))