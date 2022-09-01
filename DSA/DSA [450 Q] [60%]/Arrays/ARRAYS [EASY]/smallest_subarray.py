def func(arr,target):
    arr1 = []
    arr2 = []
    for i in range(len(arr)+1):
        for j in range(i+1,len(arr)+1):
            arr1.append(arr[i:j])
    for i in arr1:
        if sum(i) > target:
            arr2.append(i)
    
    count = len(arr2[0])
    for i in arr2:
        if len(i) < count:
            count = len(i)
    return count


            


print(func([1 ,3 ,4 ,7 ,10 ,10 ,8 ,10],10))