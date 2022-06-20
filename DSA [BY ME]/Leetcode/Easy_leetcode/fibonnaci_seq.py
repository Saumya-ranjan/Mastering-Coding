def func(x):
    if int(x)==1:
        return 1
    elif int(x)==0:
        return 0
    else:
        a,b = 0,1
        for i in range(int(x)-1):
            c = a+b
            a = b
            b = c
        return c


def apply(y):
    if y == 0:
        print('0')
    elif y == 1:
        print('1')
    else:
        print(func(y-1)+func(y-2))

apply(int(input("Enter a number: ")))