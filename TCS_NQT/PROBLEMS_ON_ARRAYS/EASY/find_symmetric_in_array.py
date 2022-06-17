def func(arr):
    arr1 =[]
    for i in arr:
        if i[::-1] in arr:
            if arr.index(i) < arr.index(i[::-1]):
                if i[::-1] not in arr1:
                    arr1.append(i[::-1])
    print(arr1)
    



func([[1,5],[2,3],[4,2],[5,1],[2,4]])