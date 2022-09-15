# INORDER TRAVERSAL
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def printInorder(root , arr):
    if root != None:
        printInorder(root.left ,arr )
        arr.append(root.val)
        printInorder(root.right , arr)
    return arr
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(printInorder(root , []))




# PREORDER TRAVERSAL
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def preorder(root,arr):
    if root!= None:
        arr.append(root.val)
        preorder(root.left,arr)
        preorder(root.right,arr)
    return arr
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(preorder(root,[]))




# POSTORDER TRAVERSAL
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def postorder(root,arr):
    if root!= None:
        postorder(root.left,arr)
        postorder(root.right,arr)
        arr.append(root.val)      
    return arr
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(postorder(root,[]))