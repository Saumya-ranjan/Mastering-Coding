class Solution:
    def combinationSum3(self  , k , n):
        arr = [1,2,3,4,5,6,7,8,9]
        res = []
        self.dfs(k,n,[],res,arr)
        return res
    def dfs(self, k , target , path, res, arr):
        if k == 0 and target == 0:
            res.append(path)
        elif k < 0 or target < 0:
            return 
        else:
            for i in range(len(arr)):
                self.dfs( k-1 , target - arr[i] , path+[arr[i]] , res , arr[i+1:])
            
a = Solution()
print(a.combinationSum3(3,7))