def func(arr):
    arr1 = []
    for i in arr.split():
        arr1.append(i)
    arr1.sort(key=len)
    print(arr1[-1])


func("Microsoft Teams")