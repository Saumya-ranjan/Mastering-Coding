def func(A):
    press = 0
    for i in A:
        if (i == 1 and press % 2 == 1) or (i == 0 and press % 2 == 0):
            press += 1
    print(press)


func([1,0,1,0])