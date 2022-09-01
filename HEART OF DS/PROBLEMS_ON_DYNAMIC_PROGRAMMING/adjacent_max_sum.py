def func(arr):
    dp = [0 for i in range(len(arr)+1)]
    for i in range(len(arr)):
        dp[i+1] = arr[i]
    for i in range(2,len(dp)):
        dp[i] += max(dp[:i-1])
    return dp
   
print(func([8,8,232,42,332,3,4,532,23]))