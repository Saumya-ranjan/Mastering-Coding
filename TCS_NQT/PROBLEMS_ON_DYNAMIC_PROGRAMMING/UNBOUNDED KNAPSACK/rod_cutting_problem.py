# Same as unbounded knapsack --> asked in a different way:
# Just twisted the Question of Unbounded Knapsack

# As, we cut down the length of rod then we can use the same length again in knapsack
# as 1m length of rod can be put in knapsack again and again so it is of unbounded 
def rod_cutting_problem(length,profit,L):
    length1 = []
    for i in range(length):
        length1.append(i+1)
    dp = [[0 for _ in range(L+1)] for _ in range(len(length1)+1)]
    for i in range(len(dp)):
        for j in range(L+1):
            if length1[i-1] <= j:
                dp[i][j] = max(profit[i-1]+dp[i][j-length1[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)


rod_cutting_problem(9,[1,2,3,4,5,6,7,8,90],18)