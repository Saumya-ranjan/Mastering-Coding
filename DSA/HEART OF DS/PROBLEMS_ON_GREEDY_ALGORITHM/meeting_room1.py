def func(arr):
    arr.sort()
    print(arr)
    arr1 = [arr[0]]
    for i in arr[1:]:
        if i[0] < arr1[-1][-1]:
            return False
        arr1.append(i)
    return True



print(func([[0,10],[19,40],[10,20]]))