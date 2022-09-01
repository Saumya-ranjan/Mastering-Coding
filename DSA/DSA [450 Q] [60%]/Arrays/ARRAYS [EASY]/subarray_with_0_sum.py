def func(arr):
    count = 0
    arr1 = []
    for i in range(len(arr)+1):
        for j in range(i+1,len(arr)+1):
            arr1.append(arr[i:j])
    print(arr1)
    for i in arr1:
        if sum(i) == 0:
            count+=1
    if count > 0:
        return 'Yes' 
    return 'No'


print(func([1,2,3, 4, 5]))