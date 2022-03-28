def func(x,target):
    a = 0
    for i in range(1,int((len(x)/target)+2)):
        print(x[a:target*i])
        a = target*i
    



func('asdfghyrhrongwhh',2)