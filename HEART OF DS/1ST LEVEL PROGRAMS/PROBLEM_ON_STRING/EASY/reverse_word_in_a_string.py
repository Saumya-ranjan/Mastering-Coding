def func(a):
    b  = ""
    arr = []
    for i in a.split():
        arr.append(i)
    arr = arr[::-1]
    for i in arr:
        b+= i+' '
    print(b)



func("This is decent")