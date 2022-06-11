#Tabulation

def func(x):
    dp = [0 for i in range(x+1)]
    dp[1] = 1
    for i in range(2,len(dp)):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[x]
print(func(200))

# Brute Force

# def func(x):
#     a = 1
#     b = 1
#     if x == 1 or x==2:
#         return 1
#     for i in range(x-2):
#         c = a+b
#         a,b = c,a
#     return c  
# print(func(100))