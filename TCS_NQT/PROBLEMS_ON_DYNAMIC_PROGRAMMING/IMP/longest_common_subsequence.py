#DYNAMIC WAY --> TABULATION APPROACH [TABLES]
# 2D ARRAY IN PYTHON --> DYNAMIC WAY
def func(str1,str2):
    dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
    for i in range(len(str2)):
        for j in range(len(str1)):
            if str2[i] == str1[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    print(dp[-1][-1])

func("abcde","ace")