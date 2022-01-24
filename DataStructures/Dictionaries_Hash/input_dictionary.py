def problem():
    x = {}
    i = int(input("Enter a Number for dictionary: "))
    for k in range(i):
        y=str(input("Enter value: "))
        z=y.split(" ")
        x[z[0]]=z[1]

    print(x)
    x.pop('name')
    print(x)



problem()