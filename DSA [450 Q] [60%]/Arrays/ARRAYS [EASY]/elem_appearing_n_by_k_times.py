def func(arr,k):
    arr1 = []
    target = len(arr)/k
    hash= {}
    for i in arr:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i]+=1
    for r in hash.keys():
        if hash[r] > target:
            arr1.append(r)

    print(arr1)

    


func([3, 1, 2, 2, 1, 2, 3, 3],4)