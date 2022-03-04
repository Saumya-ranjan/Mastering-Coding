def func(x):
    a = str(x)
    b =""
    arr = []
    for i in range(len(a)):
        arr.append(a[i])
    for j in range(len(arr)):
        if arr[j] == '6':
            arr[j]='9'
            break
    for k in arr:
        b+=k
    c = int(b)
    print(c)

func(9669)