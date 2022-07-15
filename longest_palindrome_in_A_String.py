def func(S):
    a = S[::-1]
    dp = [[0 for _ in range(len(S)+1)] for _ in range(len(a)+1)]
    for i in range(1,len(dp)):
        for j in range(1,len(S)+1):
            if a[i-1] == S[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = 0
    



func("aaaabbaa")