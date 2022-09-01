def func(start,end):
    interval = list(zip(start,end))
    interval = sorted(interval, key = lambda x: x[1])

    # lamda: One Liner function
    # lamda x,y: x-y
    prev = 0
    result = 1
    for i in range(1,len(interval)):
        if interval[i][0] > interval[prev][1]:
            result+=1
            prev = i
    return result


print(func([1,3,0,5,8,5],[2,4,6,7,9,9]))