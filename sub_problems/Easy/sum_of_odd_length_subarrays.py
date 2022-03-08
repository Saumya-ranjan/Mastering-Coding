def func(x):
    arr = []
    count = 0
    for i in range(len(x)+1):
        for j in range(i+1,len(x)+1):
            sub  = x[i:j]
            arr.append(sub)
    for j in arr:
        if len(j)%2 !=0:
            count+=sum(j)

    print(count)

func([1,4,2,5,3])