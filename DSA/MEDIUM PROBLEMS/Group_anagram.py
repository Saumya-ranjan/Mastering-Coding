def groupAnagrams(strs):
    hash = {}
    arr1 = []
    for i in strs:
        a = ''.join(sorted(i))
        if str(a) not in hash:
            hash[str(a)] = [i]
        else:
            hash[str(a)].append(i)
    for i in hash.values():
        arr1.append(i)
    return arr1
groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        