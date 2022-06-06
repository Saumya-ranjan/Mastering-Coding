def func(arr):
    arr1 = []
    for i in range(len(arr)):
        j = max(arr[i+1:],default = -1)
        arr1.append(j)
    print(arr1)

func( [17,18,5,4,6,1])