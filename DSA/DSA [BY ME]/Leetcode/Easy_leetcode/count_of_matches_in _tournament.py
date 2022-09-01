def func(n):

    matches = 0
    count = 0
    while n !=1:
        if n%2 == 0:
            matches = int(n/2)
            count+=matches
            n = int(n/2)
        else:
            matches = int((n-1)/2)
            n = int((n+1)/2)
            count+=matches
    print(int(count))
        


func(3)