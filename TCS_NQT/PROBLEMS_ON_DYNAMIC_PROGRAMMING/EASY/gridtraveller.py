def func(m,n):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(len(dp)):
        for j in range(m):
            if i == 0 or j ==0 :
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

func(3,2)