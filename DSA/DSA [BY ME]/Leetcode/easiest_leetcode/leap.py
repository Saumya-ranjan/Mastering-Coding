def func(year):
    if year % 4 !=0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            if year % 400 != 0:
                return False
            else:
                return True
            

print(func(2000))