# BASIC STYLE

# def func():                   
#     x = int(input("Enter the Number: "))
#     value = 1
#     for i in range(1,x+1):
#         value = value*i
#     print(f"The factorial of {x} is: {value}")
# func()

# USING RECURSION

def func(x):
    
    if x == 1:
        return 1
    else:
        return x*func(x-1)


print(func(int(input("Enter a Number: "))))