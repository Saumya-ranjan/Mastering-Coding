# Same as the Fibonacci series:

def func(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2,len(dp)):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]



print(func(6))