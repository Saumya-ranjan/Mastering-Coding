class Solution:
    def combine(self,n,k):
        # DFS
        arr = []
        res = []
        for i in range(1,n+1):
            arr.append(i)
            
        self.dfs(arr,k,[],res)
        return res
    
    def dfs(self,arr,k,path,res):
        if k == 0:
            res.append(path)
        elif k < 0:
            return 
        else:
            for i in range(len(arr)):
                self.dfs(arr[i+1:] , k-1 , path+[arr[i]] , res)
a =  Solution()
print(a.combine(4,2))
        