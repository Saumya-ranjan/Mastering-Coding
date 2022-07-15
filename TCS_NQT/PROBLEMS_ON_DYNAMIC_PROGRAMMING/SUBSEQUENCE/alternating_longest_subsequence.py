# Its easy just check in one-d array
def AlternatingaMaxLength(nums):
    dp = [0 for _ in range(len(nums))]
    dp[0] = 1
    if len(nums) == 1:
        return 1
    elif nums[1] >= nums[0]:
        flag = "up"
    else:
        flag = "down"
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1] and flag == "up":
            dp[i] = dp[i-1]+1
            flag = "down"
        elif nums[i] < nums[i-1] and flag =="down":
            dp[i] = dp[i-1]+1
            flag = "up"
        else:
            dp[i] = dp[i-1]
    return dp[-1]
AlternatingaMaxLength([1,5,4])
	        