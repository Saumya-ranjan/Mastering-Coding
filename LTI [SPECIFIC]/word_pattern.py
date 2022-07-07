def wordPattern(s, p):
    hash = {}
    words= s.split(' ')
    if len(p) != len(words): 
        return 'No'
    if len(set(p)) != len(set(words)): 
        return 'No' 
    for i in range(len(words)):
        if words[i] not in hash: 
            hash[words[i]] = p[i]
        elif hash[words[i]] != p[i]: 
            return "No"
    return "Yes"
print(wordPattern('hen hen hen hen','aaaa'))