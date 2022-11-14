class Solution:
    def minimumDeleteSum(s1,s2):
        # Dp Sum  -- >
        
        dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        i_sum = 0
        j_sum = 0
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i == 0 and j==0:
                    dp[i][j] = 0 
                elif i==0:
                    i_sum += ord(s2[j-1])
                    dp[i][j] = i_sum
                elif j == 0:
                    j_sum +=ord(s1[i-1])
                    dp[i][j] = j_sum
        
        for i in range(len(dp)):
            for j in range(len(dp[i])):  
                if i==0 and j==0:
                    dp[i][j] = 0
                elif s1[i-1] == s2[j-1] and i!=0 and j!=0:
                    dp[i][j] = dp[i-1][j-1]
                elif s1[i-1]!= s2[j-1] and i!=0 and j!=0:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]) , dp[i][j-1] + ord(s2[j-1]))
        return dp[-1][-1]