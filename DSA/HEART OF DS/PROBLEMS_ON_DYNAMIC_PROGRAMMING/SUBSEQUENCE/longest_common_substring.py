def longest_common_substring(str1,str2):
    dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if str1[j-1] == str2[i-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = 0
    arr = []
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            arr.append(dp[i][j])
    print(arr)




longest_common_substring('abcdrtuyutertg','abcdhgrtuyutghtt')