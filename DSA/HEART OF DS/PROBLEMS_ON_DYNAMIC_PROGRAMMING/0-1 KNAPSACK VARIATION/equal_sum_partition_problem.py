def equal_sum_partition(arr):
    target = int(sum(arr)/2)
    dp = [[False for _ in range(target+1)] for _ in range(len(arr)+1)]
    if sum(arr)%2 != 0:
        return False
    for i in range(len(dp)):
        for j in range(target+1):
            if j == 0:
                dp[i][j] = True
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)

equal_sum_partition([5,5,1,11])