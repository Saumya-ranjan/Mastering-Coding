class Solution:
    def countGoodStrings(self , low , high  , zero , one):
        MOD = 10**9 + 7
        
        ans = 0
        dp = [-1 for _ in range(high+1)]
        for i in range(low,high+1):    
            ans+= self.solve(i , zero , one , dp )
        return ans%MOD
    
    def solve(self , target , zero , one , dp):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if dp[target]!=-1:
            return dp[target]
        dp[target] = self.solve(target - zero , zero , one , dp) + self.solve(target - one , zero , one , dp)
        return dp[target]