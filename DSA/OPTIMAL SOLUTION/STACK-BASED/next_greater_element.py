class Solution:
    def nextGreaterElements(nums):
        # MONOTONIC STACK:
        stack = []
        k = len(nums)
        nums.extend(nums)
        dp = [0 for _ in range(len(nums))]
        a = nums[::-1]
        for i in range(len(a)):
            while len(stack) != 0:
                if a[i] >= stack[-1]:
                    stack.pop()
                else:
                    dp[i] = stack[-1]
                    stack.append(a[i])
                    break
            if len(stack) == 0:
                stack.append(a[i])
                dp[i] = -1
        return dp[len(dp)-1:(len(dp) - k)-1:-1 ]
                
        
        # # TLE: 
        
        
        # a = len(nums)
        # print(a)
        # nums.extend(nums)
        # dp = [0 for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(i+1,len(nums)):
        #         count+=1
        #         if nums[j] > nums[i]:
        #             dp[i] = nums[j]
        #             break   
        #     if count == len(nums) - (i+1):
        #         dp[i] = -1
        #     count = 0
        # return dp[:a]