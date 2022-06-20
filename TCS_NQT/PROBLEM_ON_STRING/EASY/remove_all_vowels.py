def func(a):
    for i in a:
        if i in "aeiouAEIOU":
            a = a.replace(i,"")
    print(a)


func("Hey u there or why u are crying at first place")