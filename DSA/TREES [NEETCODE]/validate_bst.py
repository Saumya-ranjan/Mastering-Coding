# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(root):
        # Inorder -- >
        def inorder(node , arr):
            if node!=None:
                inorder(node.left , arr)
                arr.append(node.val)
                inorder(node.right , arr)
            return arr

            
        a = inorder(root , [])
        for i in range(1,len(a)):
            if a[i] <= a[i-1]:
                return False
        return True
                
                
    