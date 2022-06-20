def func(start,jump,length):
    arr = [start]
    for i in range(length-1):
        start+=jump
        arr.append(start)
    print(sum(arr))
        



func(-2,5,8)