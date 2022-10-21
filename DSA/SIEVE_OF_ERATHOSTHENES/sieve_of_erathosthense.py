def func(n):
    prime = [ True for _ in range(n+1)]
    p = 2
    while p**2 < n:
        for i in range(p*2 , n+1 , p):
            if prime[i] == True:
                prime[i] = False
        p+=1
    print(prime)
    for i in range(2 , len(prime)):
        if prime[i] ==True:
            print(i)
            
func(10)