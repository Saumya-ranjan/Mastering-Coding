def func(words,pref):
    count = 0
    for i in words:
        t = i[:len(pref)]
        if pref in t:
            count+=1
    print(count)
    return count
        

func(['attend','attention','alter'],'at')