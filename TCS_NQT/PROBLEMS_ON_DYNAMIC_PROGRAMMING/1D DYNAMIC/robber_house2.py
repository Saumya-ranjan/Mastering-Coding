def rob(nums):
    def house_robber(n):
        dp = [0 for _ in range(len(n))]
        for i in range(len(dp)):
            if i<2:
                dp[i] = n[i]
            else:
                dp[i] = max(dp[:i-1])+n[i]
        return max(dp[-1],dp[-2])
    if len(nums) <=2 : 
        return max([0] + nums)
    return max(house_robber(nums[1:]), house_robber(nums[:len(nums)-1]))
print(rob([2,3,2]))