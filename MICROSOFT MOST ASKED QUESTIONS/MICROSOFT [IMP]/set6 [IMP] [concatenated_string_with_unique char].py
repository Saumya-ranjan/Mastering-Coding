class Solution:
    def maxLength(self , arr):
        #BackTracking -- >
        res = []     
        self.dfs(arr , res , [])
        max_count = 0
        for i in range(len(res)):
            a = ''.join(res[i])
            if len(set(a)) == len(a):
                max_count = max(max_count , len(a))
        return max_count
            
    
    def dfs(self , arr , res , stack):
        res.append(stack)
        for i in range(len(arr)):
            self.dfs(arr[i+1:] , res , stack+[arr[i]] )
    
    