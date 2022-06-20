def func(a):
    hash = {}
    for i in a:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i]+=1
    for i in sorted(hash.keys()):
        if hash[i] >1:
            print(str(i)+" - "+str(hash[i]))



func("sinstriiintng")