def func(x):
    str1 = ""
    str2 = ""
    value = 0
    arr = []
    for i in str(x):
        arr.append(i)

    arr.sort()
    str1 = arr[0]+arr[2]
    str2 = arr[1]+arr[3]

    value = int(str1)+int(str2)
    print(value)



func(2932)