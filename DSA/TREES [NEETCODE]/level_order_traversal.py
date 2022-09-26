def levelOrder(self, root):
    if root == None:
        return []
        
    queue = [root]
    res = []
        
    while queue:
        arr = []
        for i in range(len(queue)):
            node  = queue.pop(0)
            arr.append(node.val)
            if node.left !=None:
                queue.append(node.left)
            if node.right!=None:
                queue.append(node.right)
        res.append(arr)
    return res
levelOrder([3,9,20,None,None,15,7])
                
                
                