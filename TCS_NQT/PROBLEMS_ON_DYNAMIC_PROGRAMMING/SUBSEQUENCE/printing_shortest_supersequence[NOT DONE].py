# def supersequence(str1,str2):
#     scs = ""
#     a = len(str1)
#     b = len(str2)
#     dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
#     for i in range(1,len(str2)+1):
#         for j in range(1,len(str1)+1):
#             if str2[i-1] == str1[j-1]:
#                 dp[i][j] = dp[i-1][j-1]+1
#             else:
#                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
#     while a!=0 and b!=0:
#         if str1[a-1] == str2[b-1]:
#             a-=1
#             b-=1
#             scs+=str1[a-1]
#         else:
#             if dp[b-1][a] > dp[b][a-1]:
#                 b-=1
#                 scs+=str2[b-1]
#             else:
#                 scs+=str1[a-1]
#                 a-=1
#     if a!=0:
#         scs+=str1[a-1]
#         a-=1
#     if b!=0:
#         scs+= str2[b-1]
#         b-=1

#     print(scs[::-1])


            


# supersequence("AGGTAB",'GXTXAYB')
