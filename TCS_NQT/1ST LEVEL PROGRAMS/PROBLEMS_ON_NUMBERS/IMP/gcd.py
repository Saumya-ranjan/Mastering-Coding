def func(num1,num2):
    arr = []
    arr1 = []
    arr3 = []
    for i in range(1,num1+1):
        if num1%i == 0:
            arr.append(i)
    for i in range(1,num2+1):
        if num2%i == 0:
            arr1.append(i)
    for i in arr:
        if i in arr1:
            arr3.append(i)
    print(max(arr3))



func(15,15)