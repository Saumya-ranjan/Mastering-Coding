def func(x):                  #o(n)
    arr = []
    count = int((len(x)/2))
    for i in range(int(len(x)/2)) :
        arr.append(x[i])
        arr.append(x[count])
        count+=1
    print(arr)



func([2,3,4,10])