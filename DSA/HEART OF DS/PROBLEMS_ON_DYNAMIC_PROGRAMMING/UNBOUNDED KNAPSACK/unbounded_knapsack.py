def unbounded_knapsack(arr,profit,W):
    dp = [[ 0 for _ in range(W+1)] for _ in range(len(arr)+1)]
    for i in range(len(dp)):
        for j in range(W+1):
            if arr[i-1] <= j:
                dp[i][j] = max(dp[i-1][j],profit[i-1]+dp[i][j-arr[i-1]])
                # dp[i][j-arr[i-1]] is the change because we can again take that element
                # so we can again add that element as if it is included
                # or if it is not included just ignore that and don't add it again
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)



unbounded_knapsack([1,2,3,4,9],[1,2,3,4,90],18)