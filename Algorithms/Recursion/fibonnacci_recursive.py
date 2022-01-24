# BASIC METHOD:       It's My Method

# def func(x):                               
#     arr = [1,1]
#     a=1
#     b=1
#     for i in range(x-2):
#         c = a+b
#         a=b
#         b = c
        
#         arr .append(c)
#     print(arr)
# func(int(input("Enter a Number: ")))


# RECURSIVE METHOD:  

def func(x):
    arr = []
    if x == 1:
        return 1
    else:
        return arr.append(x+func(x-1))


print(func(int(input("Enter the Number: "))))