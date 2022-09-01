def clint_number(n):
    count = 0
    # two function --> prime _function and largest prime _factorization function
    def prime(n):
        if n == 2:
            return True
        for i in range(2,n):
            if n %i ==0:
                return False
        return True
    def prime_factorization(n,i):
        if n%i == 0:
            return True
        return False

    while n!=0:
        for i in range(n-1,1,-1):
            if prime(i) == True and prime_factorization(n,i) == True:
                n = i
                count+=1
        n-=1
        count+=1
    return count

print(clint_number(20))