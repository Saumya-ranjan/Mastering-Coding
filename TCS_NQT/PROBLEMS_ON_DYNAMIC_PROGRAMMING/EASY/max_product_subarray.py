def func(arr):
    arr1= []
    arr2 = []
    for i in range(len(arr)+1):
        for j in range(i+1,len(arr)+1):
            arr1.append(arr[i:j])
    for i in arr1:
        count = 1
        for j in i:
            count *=j
        arr2.append(count)
    print(max(arr2))
            


func([1,2,-3,0,-4,-5])