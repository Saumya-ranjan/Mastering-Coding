def minFlips(s):
        cnt1 = 0
        cnt2 = 0
        
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    cnt1 += 1
                else:
                    cnt2 += 1
            else:
                if s[i] == "1":
                    cnt1 += 1
                else :
                    cnt2 += 1
        
        return min(cnt1,cnt2)
minFlips("0001010111")