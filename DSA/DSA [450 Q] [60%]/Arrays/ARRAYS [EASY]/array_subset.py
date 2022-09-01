def func(a,b):
    count = 0
    if len(a) >= len(b):
        for i in b:
            if i in a:
                count+=1
        if count == len(b):
            return True
    return False


print(func([11, 1, 13, 21, 3, 7],[11, 3, 7, 1]))