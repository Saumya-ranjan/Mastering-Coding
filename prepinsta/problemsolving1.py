# longest Substring of vowel in a string (continious)

def func(x):
    vowel = "aeiou"
    count,res = 0,0
    for i in range(len(x)):
        if x[i] in vowel:
            count+=1
        else:
            res = max(res,count)
            count= 0
    print(max(res,count))
        

func("aeiraeiou")