def func(n,r):
    count1 = 1
    count = 1
    for i in range(1,n+1):
        count*= i
    for i in range(1,(n-r)+1):
        count1*=i
    print(int(count/count1))


func(6,4)