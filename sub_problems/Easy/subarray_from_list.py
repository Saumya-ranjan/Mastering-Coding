def func(x):
    sub = [[]]
    for i in range(len(x)+1):
        for j in range(i+1,len(x)+1):
            sub_list = x[i:j]
            sub.append(sub_list)
    print(sub)


func([1,2,3])