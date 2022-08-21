# Bug -->  Only works for 5:

def func(n):
    if n%2 == 0:
        return False
    rows = col = n
    for i in range(rows):
        for j in range(col + 3):
            if(i == 0 or i == rows - 1 or j == 0 or j == col - 1 or (i == (round(rows/2)) and j > col - 1)):
                if j > col - 1:
                    if i != 2:
                        continue
                print('*', end = '  ')
            else:
                print(' ', end = '  ')
        print()


func(int(input("Enter Only valid Odd Numbers: ")))