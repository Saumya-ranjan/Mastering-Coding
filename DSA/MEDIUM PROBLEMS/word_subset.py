def wordSubsets(words1,words2):
    # Calculate Resultant String:
    arr = []
    hash1 = {}
    for i in range(len(words2)):
        hash = {}
        for j in words2[i]:
            if j not in hash:
                hash[j] = 1
            else:
                hash[j]+=1
        for k in hash.keys():
            if k not in hash1:
                hash1[k] = hash[k]
            else:
                if hash1[k] < hash[k]:
                    hash1[k] = hash[k]
    for i in words1:
        counter = 0
        for j in hash1.keys():
            if hash1[j] <= i.count(j):
                counter+=1
        if counter == len(hash1):
            arr.append(i)
    return arr
wordSubsets(["amazon","apple","facebook","google","leetcode"],["e","oo"])