# Main for dictionary 

def topKFrequent( words, k ):
    hash = {}
    arr = []
    for i in words:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i]+=1
    res = sorted(hash.items(),key =lambda x: (-x[1],x[0]))
        
    for i in range(k):
        arr.append(res[i][0])
    return arr
print(topKFrequent(["love","i","leetcode","i","love","coding"] , 2))