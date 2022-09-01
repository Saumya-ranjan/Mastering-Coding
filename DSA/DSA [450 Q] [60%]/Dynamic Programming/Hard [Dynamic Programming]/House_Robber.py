def func(arr):
    dp = [0 for i in range(len(arr)+1)]
    for i in range(len(arr)):
        dp[i+1] = arr[i]
    for i in range(2,len(dp)):
        dp[i] += max(dp[:i-1])
    return max(dp)





print(func([1,2,3,1]))