# def minCostClimbingStairs(cost):
#     if len(cost) == 0:
#         return 0
#     dp = [0 for _ in range(len(cost))]
#     dp[0] = cost[0]
#     if len(cost) >= 2:
#         dp[1] = cost[1]
#     for i in range(2, len(cost)):
#         dp[i] = cost[i] + min(dp[i-1], dp[i-2])
#     return min(dp[-1], dp[-2])
# print(minCostClimbingStairs([10,15,20]))


def func(arr):
    if len(arr) == 0:
        return 0
    dp = [0 for _ in range(len(arr))]
    dp[0] = arr[0]
    if len(arr) >=2:
        dp[1] = arr[1]
    for i in range(2,len(dp)):
        dp[i] =arr[i] +  min(dp[i-1],dp[i-2])
    return dp
print(func([10,15,20]))