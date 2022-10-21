class Solution:
    def subsets(self, nums):
        res= []
        self.dfs(res,[],nums)
        return res
    def dfs(self, res, path , nums):
        res.append(path)
        for i in range(len(nums)):
            self.dfs(res, path+[nums[i]] , nums[i+1:])
    
                
        