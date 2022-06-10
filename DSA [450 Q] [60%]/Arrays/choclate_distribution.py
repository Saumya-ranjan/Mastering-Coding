def func(arr,target):
    arr.sort()
    arr1 = []
    print(arr)
    for i in range(len(arr)):
        if i+5 <len(arr)+1:
            c = sum(arr[i:i+5])
            arr1.append(c)

    print(arr1)

func([3, 4, 1, 9, 56, 7, 9, 12],5)