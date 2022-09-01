def func(n):
    arr = []
    for i in range(1,n+1):
        if n % i == 0:
            arr.append(i)
    for i in arr:
        print(i,end = " ")



func(9)