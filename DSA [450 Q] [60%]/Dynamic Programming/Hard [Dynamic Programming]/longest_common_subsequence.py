def func(str1,str2):
    # vowel = "aeiou"
    dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
    for i in range(len(str2)):
        for j in range(len(str1)):
            if str1[j] == str2[i] :      # and str1[j] in vowel:    --> For Vowel
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    print(dp)
    print(dp[len(str2)][len(str1)])

func("vowelpunish","english")