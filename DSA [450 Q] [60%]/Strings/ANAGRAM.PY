def func(words):
     
    result=[]
    for x in range(len(words)):
        if words[x]=="-1":
            continue
        group=[words[x]]
        for y in range(x+1,len(words)):
            if words[y]!="-1":
                if set(words[x])==set(words[y]):
                    group.append(words[y])
                    words[y]="-1"
        result.append(group)
        
            
    return result

print(func(['act','god','tac','cat']))