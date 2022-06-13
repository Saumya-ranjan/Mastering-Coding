def func(matrix):
    hash = {}
    arr = []
    for i in matrix:
        for j in set(i):
            if j not in hash:
                hash[j] = 1
            else:
                hash[j]+=1
    for i in hash.keys():
        if hash[i] == len(matrix):
            arr.append(i)
    print(arr)




func([[1, 2, 1, 4, 8],
             [3, 7, 8, 5, 1],
             [8, 7, 7, 3, 1],
             [8, 1, 2, 7, 9]])