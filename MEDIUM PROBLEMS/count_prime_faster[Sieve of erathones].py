def countPrimes(n):
    if n <= 2:
        return 0
    dp = [True] * n
    dp[0] = dp[1] = False
    for i in range(2, n):
        if dp[i]:
            for j in range(i*i, n, i):
                dp[j] = False
    return sum(dp)
countPrimes(20)

      
                    
# def countPrimes(n):
#     if n <2:
#         return 0
#     for i in range(2,n):
#         if n % i == 0:
#             return 0
#     return n

    
# print(countPrimes(2))