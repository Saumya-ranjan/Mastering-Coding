#DYNAMIC PROGRAMMING
def func(str1):
    str2 = ""
    for i in reversed(str1):
        str2+=i
    def palindromic(str1,str2):
        dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
        for i in range(len(str2)):
            for j in range(len(str1)):
                if str2[i] == str1[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]
    res = palindromic(str1,str2)
    return res

print(func("bbbab"))


# #   Recursive ways (Brute force method)

# def func(s):
#     arr = []
#     def subsequence(s,output,arr):
#         if len(s) == 0:
#             if output == output[::-1]:
#                 arr.append(output)
#                 return
#             return
#         subsequence(s[1:],output+s[0],arr)   # Recursive
#         subsequence(s[1:],output,arr)
#     subsequence(s,"",arr)
#     arr.sort(key = len)
#     arr = arr[::-1]
#     return len(arr[0])

# o(n^2)  -> 70 cases/89

# print(func("bbab"))