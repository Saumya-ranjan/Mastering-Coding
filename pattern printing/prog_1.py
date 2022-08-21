# o(n) --> time complexity: 
def func(side):
    if side% 2 ==0 or side < 5:
        return False
    for i in range(int(side /2) ):
        for j in range(side):
            if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
                print('*', end = '  ')
            else:
                print(' ', end = '  ')
        print()
    for i in range(side):
        print("*" , end = '  ')
    print()
    count = 1
    for i in range(side - (int(side/2) + 1)):
        if side == 5:
            print(" "*(side+count)+"*")
        else:
            print(" "*(side+4)+"*")

print(func(int(input("only enter odd numbers: "))))


