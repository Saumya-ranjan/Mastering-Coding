# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self,root,targetSum):
        self.ans = 0
        self.dfs(root , targetSum)
        return self.ans
    
    def dfs(self , root , target):
        if root == None:
            return 
        self.stack(root , target)
        self.dfs(root.right , target)
        self.dfs(root.left , target)
        
    def stack(self , root , target):
        if root ==None:
            return 
        if root.val == target:
            self.ans+=1
        self.stack(root.right , target-root.val)
        self.stack(root.left , target - root.val)
        