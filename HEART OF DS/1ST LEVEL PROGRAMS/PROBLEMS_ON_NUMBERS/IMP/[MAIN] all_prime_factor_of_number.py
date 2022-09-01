def func(n):
    arr = []

    for i in range(2,n):
        if n %i ==0:
            while n%i == 0:   # Until n is not divisible by i till then do divide it 
                arr.append(i)
                n = n/i
    print(arr)


func(36)