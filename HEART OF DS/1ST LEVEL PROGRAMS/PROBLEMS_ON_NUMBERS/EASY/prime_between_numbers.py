def func(a,b):
    arr = []
    for i in range(a,b+1):
        if i > 1:
            count = 0
            for j in range(2,i):               
                if i%j == 0:
                    count+=1
            if count ==0:
                arr.append(i)
    print(arr)



func(1,100)