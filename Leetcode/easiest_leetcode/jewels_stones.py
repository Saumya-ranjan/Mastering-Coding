# def func(x):                # o(n)^2
#     count=0
#     jewels = input("enter the character of jewel: ")
#     for i in x:
#         for j in jewels:
#             if i == j:
#                 count+=1
#     print(count)

# func("aAAbbbb")

def func(x):                #o(n)
    count=0
    jewels = input("enter the character of jewel: ")
    for i in x:
        if i in jewels:
            count+=1
    print(count)

func("aAAbbbb")
