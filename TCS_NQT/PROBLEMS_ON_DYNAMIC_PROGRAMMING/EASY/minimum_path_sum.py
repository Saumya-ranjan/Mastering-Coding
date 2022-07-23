def minPathSum(dp):
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i>0 and j>0:
                    dp[i][j] = min(dp[i-1][j] +dp[i][j], dp[i][j-1]+dp[i][j])
                elif i>0:
                    dp[i][j] = dp[i-1][j]+dp[i][j]
                elif j>0:
                    dp[i][j] = dp[i][j-1] + dp[i][j]
        return dp[-1][-1]
minPathSum([[1,3,1],[1,5,1],[4,2,1]])
                    