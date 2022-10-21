# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(root):
        res = 0 
        def dfs(root):
            nonlocal res
            if root == None:
                return 0 , 0
            own_value , left_sum = dfs(root.left)
            own_value1 , right_sum = dfs(root.right)
            result = root.val+ left_sum + right_sum
            c = 1 + own_value + own_value1
            if result  // c == root.val:
                res+=1
            
            return c , result
        dfs(root)
        return res
    
 