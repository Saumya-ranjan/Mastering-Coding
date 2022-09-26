# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        def right_view(node, depth):
            if node!=  None:
                if depth == len(view):
                    view.append(node.val)
                right_view(node.right , depth+1)
                right_view(node.left , depth+1)
        
        view  = []
        right_view(root , 0)
        return view
    rightSideView([1,2,3,None,5,None,4])
        
    