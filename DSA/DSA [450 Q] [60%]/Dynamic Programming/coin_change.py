# def func(arr,target):
#     arr1 = []
#     dp = [None for i in range(target+1)]
#     for i in range(len(dp)):
#         if dp[i]!=None:
#             for j in arr:
#                 if i+j <len(dp):                 
#                     dp[i+j] = [*dp[i],j] 
#         if dp[target] not in arr1:
#             arr1.append(dp[target])
#     print(arr1)
#     return dp[target]
# print(func([1,2,3],4))

def count(S,n): 
        dp=[[0 for _ in range(n+1)]for _ in range(len(S)+1)]
        dp[0][0]=1
        print(dp)
        for i in range(1,len(S)+1):
            dp[i][0]=1
        for i in range(1,n+1):
            dp[0][i]=0
        for i in range(1,len(S)+1):
            for j in range(1,n+1):
                if S[i-1]<=j:
                    dp[i][j]=dp[i-1][j]+dp[i][j-S[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(S)][n]
print(count([1,2,3],5))