def print_longest_common_subsequence(str1,str2):
    a = len(str1)
    b = len(str2)
    longest_subsequence = ""
    dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if str2[i-1] == str1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    while a !=0 and b != 0:
        if str1[a-1] == str2[b-1]:
            longest_subsequence += str1[a-1]
            a-=1
            b-=1
        else:
            if dp[b-1][a] > dp[b][a-1]:
                b-=1
            else:
                a-=1
    print(longest_subsequence[::-1])




print_longest_common_subsequence('abftre','abre')


