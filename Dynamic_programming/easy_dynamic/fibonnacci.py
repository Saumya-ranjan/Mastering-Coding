# # 0 1 1 2 3 5 8
# # a = 0
# # b = 1

# def func(x):
#     arr = [0,1]
#     a = 0
#     b = 1
#     if x == 0:
#         print("")
#     elif x == 1:
#         print(arr[0])
#     elif x ==2:
#         print(arr)
#     elif x>2:
#         for i in range(x-2):
#             c = a+b
#             a = b
#             b = c
#             arr.append(c)
#         print(arr[x-1])
# func(200)

# def func(x):                       #Bottom-up Approach
#     arr = []
#     a = 0
#     b = 1
#     for i in range(x):
#         arr.append(a) 
#         a,b = b,a+b       #dont do a = b and b = a+b seperate as it changes value
          

#     print(arr)



# func(53)


def func(x):
    print(x[::-1])


func(["h","e","l","l","o"])