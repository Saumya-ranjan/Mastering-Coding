def func(arr):
    arr2 = ''
    arr1 = [arr[-1]] + arr[:len(arr)-1]
    for i in arr1:
        arr2 += str(i) + ' '
    return arr2




print(func([1,2]))