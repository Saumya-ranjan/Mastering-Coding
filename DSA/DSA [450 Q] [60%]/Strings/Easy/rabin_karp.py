def func(S,target):
    for i in range(len(S)+1):
        for j in range(i+1,len(S)+1):
            if(S[i:j]) == target:
                print(i)


func("GEEKS FOR GEEKS ","GEEK")