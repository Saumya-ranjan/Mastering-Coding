def func(str1):
    dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str1)+1)]
    for i in range(len(str1)):
        for j in range(len(str1)):
            if str1[i] == str1[j] and i!=j:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    print(dp)


func("axxzxy")