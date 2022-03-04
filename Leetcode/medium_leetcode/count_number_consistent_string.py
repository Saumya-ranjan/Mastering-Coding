def func(x,y):
    count = 0
    for i in y:
        for j in range(len(i)):
            if i[j] not in x:
                count+=1
                break
                
    print(len(y)-count)




func("ab", ["ade","bd","aaab","baa","badab"])