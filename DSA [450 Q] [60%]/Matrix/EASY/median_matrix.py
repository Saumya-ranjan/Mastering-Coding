def func(arr):
    arr1 = []
    for i in arr:
        for j in range(len(i)):
            arr1.append(i[j])
    arr1.sort()
    return arr1[int(len(arr1)/2)]



print(func([[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]))