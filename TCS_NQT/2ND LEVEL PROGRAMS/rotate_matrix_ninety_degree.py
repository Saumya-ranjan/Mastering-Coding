def func(arr):
    arr2 = []
    hash = {}
    arr = arr[::-1]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j not in hash:
                hash[j] = [].extend(arr[i][j])
    print(hash)

            

            




func([[1,2,3],[4,5,6],[7,8,9]])