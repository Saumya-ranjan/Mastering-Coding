class Solution:
    def letterCasePermutation(self,s):
        res = []
        self.dfs(s,[],res)
        return res
    def dfs(self,s,path,res):
        if len(s) == 0:
            res.append(''.join(path))
        else:
            if s[0].isupper():
                self.dfs(s[1:] , path+[s[0].lower()] , res)
            elif s[0].islower():
                self.dfs(s[1:] , path+[s[0].upper()] , res)
            self.dfs(s[1:] , path+[s[0]] , res)
        
a = Solution()
print(a.letterCasePermutation("a1b2"))