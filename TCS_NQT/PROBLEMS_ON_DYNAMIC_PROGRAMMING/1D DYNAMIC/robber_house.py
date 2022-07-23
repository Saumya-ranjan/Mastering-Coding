def rob(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    dp = [0 for _ in range(len(nums))]
    for i in range(len(dp)):
        if i < 2:
            dp[i] = nums[i]
        else:
            dp[i] = max(dp[:i-1] ) + nums[i]
    return max(dp[-1],dp[-2])
print(rob([1,2,3,1]))