def longest_palindromic_subsequence(str1):
    str2 = str1[::-1]
    dp = [[0 for _ in range(len(str1))] for _ in range(len(str2)+1)]
    for i in range(1,len(str2)):
        for j in range(1,len(str1)+1):
            if str2[i-1] == str1[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][ j-1])
    print(dp)







longest_palindromic_subsequence("ababbba") # abbbaba
