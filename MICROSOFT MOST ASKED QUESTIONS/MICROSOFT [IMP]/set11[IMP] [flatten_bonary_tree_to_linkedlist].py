
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def flatten(root):
        # ListNode for LinkedList and TreeNode for Tree
        last = TreeNode(-1)
        stack = [root]
        while len(stack)!=0:
            node = stack.pop(0)
            last.right = node
            last.left = None
            if node!=None and node.right !=None:
                stack.insert(0 , node.right)
            if node!=None and node.left!=None:
                stack.insert(0 , node.left)
            last = node
            print(last)
          