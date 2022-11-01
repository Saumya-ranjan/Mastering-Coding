# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self , root):
        # DFS -- >
        res = []
        self.dfs(root , [] , res)
        # print(res)
        ans = 0
        for k in range(len(res)):
            a = ''.join(res[k])
            ans+= int(a)
        return ans
    
    def dfs(self , root ,  path , res):
        if root == None:
            return 
        path.append(str(root.val))
        if root.right == None and root.left == None:
            res.append(list(path))
        self.dfs(root.right , path , res)
        self.dfs(root.left , path , res)
        path.pop()
    
  
    
        
            