def count_subset_sum(arr,target):
    # Knapsack 0-1
    dp = [[0 for _ in range(target+1)] for _ in range(len(arr)+1)]
    for i in range(len(dp)):
        for j in range(target+1):
            if j == 0:
                dp[i][j] = 1
            elif arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    print(dp)
            
            
    



count_subset_sum([2,3,6,7],7)