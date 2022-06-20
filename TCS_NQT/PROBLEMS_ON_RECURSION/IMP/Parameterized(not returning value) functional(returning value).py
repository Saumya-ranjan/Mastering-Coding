# PARAMATERIZED  (NOT RETURNING A VALUE)

def func(n,sume): 
    if n == 0:
        print(sume)
        return   
    func(n-1,sume+n)
func(120,0)

# FUNCTIONAL  (FOR RETURNING A VALUE)

def func(n):
    if n==0:
        return 0
    return n+func(n-1)
print(func(5))

# FACTORIAL (FUNCTIONAL)

def func(n):
    if n ==0:
        return 1
    return n*func(n-1)
print(func(5))

#FACTORIAL (PARAMETERIZED)

def func(n,fact):
    if n==0:
        print(fact)
        return 
    func(n-1,fact*n)
    
func(5,1)