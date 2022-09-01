def func(arr):
    # print(min(arr))
    temp = arr[0]
    for i in arr[1:]:
        if i<temp:
            temp = i
    return temp



print(func([2,5,1,3,0]))