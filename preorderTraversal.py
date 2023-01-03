# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    stack = []
    while root:
        res.append(root.val)
        if root.right != None:
            stack.append(root.right)
        if root.left != None:
            root = root.left
            continue
        if not stack:
            break
        root = stack.pop()
    return res
                
                       
        
