# IS A SUBSEQUENCE OF B 
# BY TABULATION METHOD NOT BY RECURSION

def is_subsequence(str1,str2):
    dp = [[0 for _ in range(len(str1)+1)] for _ in  range(len(str2)+1)]
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if str2[i-1] == str1[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    if len(str1) == dp[-1][-1]:
        return True
    return False 

print(is_subsequence('AXY','ADXCPY'))