def func(arr):
    arr.sort()
    merged=  [arr[0]]
    for i in range(1,len(arr)):
        if arr[i][0] <= merged[-1][-1]:
            merged[-1] = [merged[-1][-2],max(merged[-1][-1],arr[i][1])]
        else:
            merged.append(arr[i])
    return merged
        

        


print(func([[1,6],[3,4],[9,12],[100,200]]))