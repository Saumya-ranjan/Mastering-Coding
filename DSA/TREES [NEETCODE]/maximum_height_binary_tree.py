# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        # Recursive DFS

        #  if root==None:
        #      return 0
        #  return 1+max(self.maxDepth(root.left) , self.maxDepth(root.right))
        
        # Iterative DFS

        stack = [[root , 1]]
        res = 0
        while stack:
            node , depth = stack.pop()
            if node!=None:
                res = max(res,depth)
                stack.append([node.right , depth+1])
                stack.append([node.left , depth+1])
        return res
                
            