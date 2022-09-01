def func(start,end):
    interval = list(zip(start,end))
    interval = sorted(interval,key = lambda x: x[1])
    arr=[1]
    res = 1
    prev = 0
    for i in range(1,len(interval)):
        if interval[i][0] < interval[prev][1]:
            res+=1
            arr.append(res)
        else:
            res = 1
            prev = i
    return max(arr)

print(func([1020,1200] ,[1050,1230]))