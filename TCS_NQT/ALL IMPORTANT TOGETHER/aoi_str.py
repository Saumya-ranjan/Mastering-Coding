def func(str):
    str1 = str
    str1 = ""
    str2 = ""
    for i in str:
        str1+=i
    for i in str1:
        if i == '-':
            if len(str2) == 0:
                str2+=i
        elif i.isnumeric():
            str2+=i
    print(int(str2)) 


func("-43534")