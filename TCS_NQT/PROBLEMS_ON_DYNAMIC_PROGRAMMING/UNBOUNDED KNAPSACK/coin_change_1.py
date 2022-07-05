def coin_change(arr,target):
    # unbounded knapsack Used : Because of infinite Number of Coins
    dp = [[0 for _ in range(target+1)] for _ in range(len(arr)+1)]
    for i in range(len(dp)):
        for j in range(target+1):
            if i==0 and j==0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = 1
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i-1]]
            else:
               dp[i][j] =  dp[i-1][j]
    print(dp)
coin_change([1,2,3],5)