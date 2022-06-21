def func(a,b):
    c = 10
    def area(a,b,c):
        return a+b+c
    res = area(a,b,c)
    return res

print(func(5,4))