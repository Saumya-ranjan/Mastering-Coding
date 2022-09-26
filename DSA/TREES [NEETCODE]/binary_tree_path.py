# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(root):
        if root == None:
            return []
        stack = [(root , str(root.val))]
        res = []
        while stack:
            node , a = stack.pop() 
            if node.left == None and node.right == None:
                res.append(a)
            if node.left!=None:
                stack.append((node.left , a+"->"+str(node.left.val)))
            if node.right!=None:
                stack.append((node.right , a+"->" + str(node.right.val)))
        return res