# Recursive

# def lcs(str1,str2,count):
#     if len(str1) == 0 or len(str2) == 0:
#         return count
#     elif str1[-1] == str2[-1]:
#         count+=1
#         return lcs(str1[:-1],str2[:-1],count)
#     else:
#         return max(lcs(str1[:-1],str2,count),lcs(str1,str2[:-1],count))
# print(lcs('abcdgh','habedf',0))

def longest_common_subsequence(str1,str2):
    dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if str2[i-1] == str1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print(dp)


longest_common_subsequence('ababbba','abbbaba')


