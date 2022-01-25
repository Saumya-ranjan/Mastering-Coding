# BASIC METHOD: Iterative one       It's My Method

#Anything can be done recursively can be done iteratively(loop) too.

def func(x):                            #O(n)                 
    arr = [1,1]
    a=1
    b=1
    for i in range(x-2):
        c = a+b
        a=b
        b = c
        
        arr .append(c)
    print(arr)
func(int(input("Enter a Number: ")))


# RECURSIVE METHOD:    [This is Slow and Not time efficient]

# [0,1,1,2,3,5,8,13,21]

# def func(x):                                 #o(2^n)
#     arr = []
#     if x < 2:
#         return x
   
#     return func(x-1)+func(x-2)


# print(func(int(input("Enter the Number: "))))