# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        # Base Case
        if root == None:
            return None
        
        # Swapping childrens
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # Recursive call
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root
        
        