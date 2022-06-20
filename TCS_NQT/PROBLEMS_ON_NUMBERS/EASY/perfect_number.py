def func(n):
    arr = []
    for i in range(1,n):
        if n % i ==0:
            arr.append(i)
    if sum(arr) == n:
        print("Perfect Number")
    else:
        print("Not Perfect Number")


func(6)