# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self , root , targetSum):
        res = []
        self.dfs(root , targetSum , [] , res)
        return res
    
    def dfs(self , root , target ,arr , res):
        if root == None:
            return
        arr.append(root.val)
        if root.left == None and root.right == None and root.val == target:
            res.append(list(arr))
        self.dfs(root.right , target - root.val , arr , res)
        self.dfs(root.left , target - root.val , arr  , res)
        arr.pop()

# Remember this dfs formula recursion formula everytime u work it is very important in this Field