def func(x):
    a,b = 0,1
    for i in range(int(x)):
        a,b = b,a+b
    print(a)



func(1)