# Jump Game
def canJump(nums):
    # Dynamic programaming
    last_element  = len(nums) -1
    for i in range(last_element - 1 , -1,-1):
        if i + nums[i] >= last_element:
            last_element = i
    if last_element == 0:
        return True
    return False


# Jump Game 2
# Dp -- > o(n^2)

class Solution:
    def jump(self, nums):
        dp = [0 for _ in range(len(nums))]
        dp[0] = 0
        for i in range(len(dp)):
            for j in range(i+1,len(dp)):
                if (i+nums[i])>=j and (dp[j] == 0):
                    dp[j] = dp[i] + 1
        return dp[-1]

# Dp --> o(n)



        