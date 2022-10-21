class Solution:
    def minSwaps(s):
        s=list(s)
        count = 0
        balance = 0
        for i in range(len(s)):
            if s[i] == '[':
                balance+=1
            else:
                balance-=1
            if balance == -1:
                balance = 1
                count+=1
                
        return count
                    