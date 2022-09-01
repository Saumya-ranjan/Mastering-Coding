def func(arr):
    arr = sorted(arr)
    arr2 = [arr[0]]
    if len(arr) == 0:
        return arr
    for i in range(1,len(arr)):
        if arr[i][0] <= arr2[-1][-1]:
            arr2[-1] = [min(arr2[-1][0],arr[i][0]),max(arr2[-1][1],arr[i][1])]
        else:
            arr2.append(arr[i])
    return arr2



print(func([[2,3],[4,5],[6,7],[8,9],[1,10]]))