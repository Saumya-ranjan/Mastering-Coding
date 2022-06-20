# Recursion 1 to N:
def func(n):
    print(n)
    if n==0:
        return 
    func(n-1)      
func(5)

# Recursion N to 1:
def func(i,n):
    print(i)
    if i==n:
        return 
    func(i+1,n)
func(0,10)

