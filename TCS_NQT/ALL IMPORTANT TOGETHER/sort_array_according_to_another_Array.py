def func(arr,arr1):
    arr3 = []
    hash = {}
    arr2 = []
    arr4 = []
    for i in arr:
        if i in arr1:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i]+=1
        else:
            arr3.append(i)
    arr3.sort()
    for i in arr1:
        for j in hash.keys():
            if i ==j:
                arr2.append([i]*hash[j])
   
    for i in arr2:
        for j in i:
            arr4.append(j)
    for i in arr3:
        arr4.append(i)
    print(arr4)

func([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8, 7, 5, 6, 9, 7, 5 ],[ 2, 1, 8, 3, 1])