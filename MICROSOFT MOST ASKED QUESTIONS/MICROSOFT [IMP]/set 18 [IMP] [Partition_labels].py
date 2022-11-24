class Solution:
    def partitionLabels(s):
        hash = {}
        for i in range(len(s)):
            hash[s[i]] = i
        res = [0]        
        end = 0
        for i in range(len(s)):
            if hash[s[i]] > end:
                end = hash[s[i]]
            if end == i:
                res.append((i+1) - sum(res))
        res.pop(0)
        return res