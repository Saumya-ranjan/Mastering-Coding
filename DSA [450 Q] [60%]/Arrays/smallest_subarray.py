def func(arr,target):
    arr1 = []
    arr2 = []
    arr3 = []
    for i in range(len(arr)+1):
        for j in range(i+1,len(arr)+1):
            arr1.append(arr[i:j])
    for i in arr1:
        if len(i) ==1 and sum(i) > target:
            return 1
        elif sum(i)>target:
            arr2.append(i)
    
    curr_sum = sum(arr2[0])
    for i in arr2[1:]:
        if sum(i) < curr_sum:
            curr_sum = sum(i)
            arr3.append(i)
    return len(arr3)

            


print(func([6,3,4,5,4,3,7,9],16))