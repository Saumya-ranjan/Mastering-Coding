def func(n):
    vowel = 0
    count = 0
    space = 0
    for i in n:
        if i in "aeiouAEIOU":
            vowel+=1
        elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            count+=1
        elif i == " ":
            space+=1
    print(vowel,count,space)




func("Take u forward is  Awesome")