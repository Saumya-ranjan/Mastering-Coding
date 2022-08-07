def checkInclusion(s1,s2):
    #Anagram
    #o(n^2)
    hash1 = {}
    for i in s1:
        if i not in hash1:
            hash1[i] = 1
        else:
            hash1[i]+=1
    a = len(s1)
    for i in range(len(s2)):
        b = s2[i:i+a]
        hash = {}
        if len(b) == a:
            for j in b:
                if j not in hash:
                    hash[j] =1
                else:
                    hash[j]+=1
            if hash == hash1:
                return True
    return False
checkInclusion("ab", "eidbaooo")