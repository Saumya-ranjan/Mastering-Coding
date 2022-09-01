# KNAPSACK --> wt = [] , profit = [], W
#KNAPSACK --> BAG 
                             # knapsack ==> 1) 0-1 knapsack
                                            #2) FRACTIONAL KNAPSACK
                                            #3) unbounded knapsack 
# RECURSION 

# def knapsack(wt,profit,W):
#     # 1) base case  -> smallest value of input 
#     if len(wt) == 0 or W ==0:
#         return 0
    
#     # 2) choice condition
#     if wt[-1] <= W:
#         return max((profit[-1] + knapsack(wt[:-1],profit[:-1],W-wt[-1])),knapsack(wt[:-1],profit[:-1],W))
#     elif wt[-1] > W:
#         return knapsack(wt[:-1],profit[:-1],W)
# print(knapsack([1,4,3,6,7,9],[1,3,5,23,12,90],20))


# Tabulation

def knapsack(wt,profit,W):
    dp = [[0 for _ in range(W+1)] for _ in range(len(wt)+1)]
    for i in range(1,len(dp)):
        for j in range(1,W+1):
            # BASE CASE
            if wt[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],profit[i-1]+dp[i-1][j-wt[i-1]])
    print(dp)


knapsack([1,4,3,6,7,9],[1,3,5,23,12,90],20)

# --> Because One item could only be taken once so don't assume it twice