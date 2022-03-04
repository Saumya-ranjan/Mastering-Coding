def func(s,t):

    start = 0
    for i in s:
        c = t.find(i,start)
        if c == -1:
            return False
        start = c + 1
    return True
 
            

print(func(  "ab","ba" ))