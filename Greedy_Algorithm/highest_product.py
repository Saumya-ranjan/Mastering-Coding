def func(x):
    arr =[]
    for a in x:
        arr.append(abs(a))
    
    arr.sort()
    arr.reverse()
    
    a = arr[:3]
    count = 1
    for i in a:
        count*= i
    print(count)
    

func([ -10000000, 1, 2, 3, 4 ] )