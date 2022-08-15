class Solution:
    def combinationSum(self,candidates,target):
        res =  []
        self.dfs(candidates, target , res , [])
        return res
    def dfs(self,candidates,target,res,path):
        if target == 0:
            res.append(path)
        elif target<0:
            return 
        else:
            for i in range(len(candidates)):
                self.dfs(candidates[i:] , target - candidates[i] , res , path+[candidates[i]])
            
a  = Solution()
print(a.combinationSum([2,3,6,7] , 7))