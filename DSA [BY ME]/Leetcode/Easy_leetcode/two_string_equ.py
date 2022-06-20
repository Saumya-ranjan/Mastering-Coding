def func(x,y):
    word1=""
    word2 =""
    for i in x:
        word1+=i
    
    for j in y:
        word2+=j
    
    if sorted(word1)==sorted(word2):
        print("true")




func(["ab","c"],["a","bc"])