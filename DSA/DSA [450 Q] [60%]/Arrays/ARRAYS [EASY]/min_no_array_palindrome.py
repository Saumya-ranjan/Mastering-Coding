def func(arr):
    count = 0
    for i in arr:
        a = str(i)
        if a == a[::-1]:
            count+=1
    if count == len(arr):
        return True
    return False


print(func([111,222,333,444,556]))