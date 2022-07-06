def repeating_subsequence(str1):
    dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str1)+1):
            if str1[i-1] == str1[j-1] and i!=j:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print(dp)


repeating_subsequence("babad")