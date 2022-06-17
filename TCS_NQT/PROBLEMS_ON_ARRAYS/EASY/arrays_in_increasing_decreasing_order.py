def func(arr):
    arr1 = []
    if len(arr) %2 == 0:
        arr.sort()
        arr1.extend(arr[:int(len(arr)/2)])
        arr1.extend(arr[int(len(arr)):int((len(arr)/2)-1):-1])
    print(arr1)


func( [8 ,7 ,1, 6 ,5 ,9])