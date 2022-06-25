def func(arr):
    # return round((len(arr)-1)/2)
    arr1 = []
    hash = {}
    for i in arr:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] +=1
    for i in hash.keys():
        if hash[i] > round((len(arr)-1)/2):
            arr1.append(i)
    return arr1




print(func(  [4,4,2,4,3,4,4,3,2,4]))