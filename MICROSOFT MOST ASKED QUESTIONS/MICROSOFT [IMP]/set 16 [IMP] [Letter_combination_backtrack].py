class Solution:
    def letterCombinations(digits):
        hash = {2:'abc', 3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res = []
        def dfs(pointer, ans):
            if len(ans) == len(digits):
                res.append(ans)
                return 
            for i in hash[int(digits[pointer])]:
                dfs(pointer+1 , ans+i)
                   
        if len(digits)>0:
            dfs(0,"")
        return res