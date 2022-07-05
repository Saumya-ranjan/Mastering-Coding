def supersequence(str1,str2):
    dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if str1[j-1] == str2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print((len(str1) + len(str2))-dp[-1][-1])
    
    

        
supersequence("AGGTAB",'GXTXAYB')





