class Solution:
    def dailyTemperatures(temperatures):
        # Bruteforce Method:
        # dp = [0 for _ in range(len(temperatures))]
        # for i in range(len(dp)):
        #     for j in range(i+1,len(dp)):
        #         if temperatures[j] > temperatures[i]:
        #             dp[i] = j-i
        #             break
        # return dp
        
        # Stack Method to go for the solution:
        # NEXT GREATER ELEMENT:
        # O(N)
        # dp = [0]*len(temperatures)
        # count = len(temperatures) - 1
        # stack = []
        # temp_rev = temperatures[::-1]
        # for i in range(len(temp_rev)):
        #     if len(stack) == 0 or stack[-1] [0] > temp_rev[i]:
        #         stack.append([temp_rev[i] , len(temp_rev) - 1 - i])
        #     else:
        #         while len(stack)!=0 and stack[-1][0]<= temp_rev[i]:
        #             stack.pop(-1)
        #         stack.append([temp_rev[i] , len(temp_rev) - 1 - i])
        #     if len(stack) <2:
        #         dp[i] = 0
        #         count -=1
        #     else:
        #         dp[i] = stack[-2][1] -count
        #         count-=1
        # return dp[::-1]
    
    # Most Optimal:
        dp = [0]* len(temperatures)
        stack = []
        count = 1
        for i in range(len(temperatures)-1 , -1 , -1):
            if len(stack) == 0 or stack[-1][0] > temperatures[i]:
                stack.append([temperatures[i] , len(temperatures) - i])
            else:
                while len(stack)!=0 and stack[-1][0]<= temperatures[i]:
                    stack.pop(-1)
                stack.append([temperatures[i] , len(temperatures) -  i])
            if len(stack) < 2:
                dp[i] = 0
            else:
                dp[i] =  count -  stack[-2][1] 
            count+=1
            
        return dp
    dailyTemperatures( [73,74,75,71,69,72,76,73])
                