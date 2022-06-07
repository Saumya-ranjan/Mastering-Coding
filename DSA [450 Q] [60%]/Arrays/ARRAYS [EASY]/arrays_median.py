def func(arr):
    arr.sort()
    if len(arr)%2 != 0:
        return (arr[round((len(arr)/2)-0.1)])
    else:
        c =  (arr[round(len(arr)/2)])
        d = (arr[round((len(arr)/2)-1)])
        return round(((c+d)/2)-0.1)



print(func([18,15,19]))