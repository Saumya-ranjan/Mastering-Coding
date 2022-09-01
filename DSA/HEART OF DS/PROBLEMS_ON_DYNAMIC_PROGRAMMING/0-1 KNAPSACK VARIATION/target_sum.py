# Target Sum --> Variation of count of subset sum with given difference:

def target_sum(nums,target):
    if ((target+sum(nums))) %2 !=0:
        return 0
    else:
        s1 = int((target+sum(nums))/2)
    # Tabulation  --> efficient than memoization
    dp = [[0 for _ in range(s1+1)] for _ in range(len(nums)+1)]
    for i in range(len(dp)):
        for j in range(s1+1):
            if j == 0:
                dp[i][j] = 1
            elif nums[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return (dp)
print(target_sum([0,0,0,0,0,0,0,0,1], 1))