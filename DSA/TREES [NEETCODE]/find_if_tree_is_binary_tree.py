class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.data = []

def binary(root):
    
    def check(node):
        if node.left == None  and node.right == None:
            return True
        elif node.right!=None and node.left!=None:
            if node.right.val > node.val and node.left.val<node.val:
                return True
        elif node.left == None:
            if node.right.val > node.val:
                return True
        elif node.right == None:
            if node.left.val < node.val:
                return True
        return False

    if root != None :
        if check(root) == False:
            return False
        binary(root.left)
        binary(root.right)
    return True

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(13)
root.left.left = Node(0)
root.left.right = Node(5)
print(binary(root))