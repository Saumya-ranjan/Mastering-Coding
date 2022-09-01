# Brute-Force Method
def func(arr):
    arr1 = []
    arr2 = []
    arr = arr[::-1]
    a = len(arr) * len(arr)
    count = 0
    while len(arr1) < a:
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if j == count:
                    arr1.append(arr[i][j])
        count+=1
    count = 0
    for i in range(int(len(arr1)/len(arr))):
        arr2.append(arr1[count:count+len(arr)])
        count+=len(arr)
    print(arr2)   

func([[1,2,3,4],[4,5,6,6],[7,8,9,13],[10,11,12,13]])