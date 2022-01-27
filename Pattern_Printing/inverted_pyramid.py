# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

def func(x):
    value = 0
    for i in range(x,0,-1):
        value = value+1
        for j in range(1,i+1):
            print(value , end="")
        print("")



func(int(input("eNter the row: ")))