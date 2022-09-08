def characterReplacement(s,k):
    hash=  {}
    res = 0
    l= 0 
    for r in range(len(s)):
        if s[r] not in hash:
            hash[s[r]] = 1
        else:
            hash[s[r]]+=1
                
        if (r - l + 1) - max(hash.values()) > k:
            hash[s[l]] -=1
            l+=1
        res = max(res , (r-l+1))
    return res
characterReplacement( "ABAB",  2)
                
        
        