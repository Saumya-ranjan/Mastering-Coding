def func(v):
    arr = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    arr2 = []
    arr = arr[::-1]
    for i in arr:
        if i > v:
            arr.remove(i)
    for i in arr:
        while v >= i:
            v = v-i
            arr2.append(i)
    print(len(arr2))

func(49) # 500 100 100 100 50 5 2