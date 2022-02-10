# longest Substring of vowel in a string (continious)

def func(x):                #o(n)
    count,res = 0,0
    for i in x:
        if i in 'aeiou':
            count+=1
        else:
            res = max(count,res)
            count = 0
    print(max(res,count))



func("ehghgei")