#THERE IS A FORMULA OF GP 
# a*r**n + a*r**n+1

def func(a,r,n):
    arr = [a]
    for i in range(1,n):
        arr.append((a*r)**i)
    print(sum(arr))



func(3,5,2)