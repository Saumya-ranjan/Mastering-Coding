def strange_algo(a,b):
    if len(set(a))!=len(set(b)):
        return '-1'
    else:
        for i in set(a):
            if i not in set(b):
                return '-1'
    count = 0
    for i in range(len(a)):
        if a[i]!=b[i]:
            if a[i] < b[i]:
                return '-1'
            count+=1
    return count
            
    


print(strange_algo('abdee','abdde'))