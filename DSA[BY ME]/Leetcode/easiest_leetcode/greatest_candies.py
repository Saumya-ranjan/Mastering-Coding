def func(x):
    y = int(input("Enter the Number of candies you have :"))
    arr = []
    for i in range(len(x)):
        total = x[i]+y
        if total >= max(x):
            arr.append('true')
        else:
            arr.append("false")
    return arr


print(func([2,3,5,1,3]))