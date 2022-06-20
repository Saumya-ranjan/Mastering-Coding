def func(n):
    x = bin(n)
    p  = str(x)
    arr = ""
    for i in range(len(p)):
        if p[i] == 'b':
            arr = p[i+1:]
    print(int(arr))




func(28)