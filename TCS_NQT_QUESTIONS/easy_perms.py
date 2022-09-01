def perms(members):
    def fact(n):
        count = 1
        for i in range(1,n+1):
            count*=i
        return count
    return 2 * fact(members-1)  

print(perms(50))