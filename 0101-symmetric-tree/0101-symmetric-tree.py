# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        
        #preorder
        def check(node1,node2):
            if not node1 and not node2:
                return True
            if not (node1 and node2):
                return False
            
            if node1.val !=node2.val:
                return False 
            
            l = check(node1.left,node2.right)
            r = check(node1.right,node2.left)
            
            return (l and r)
        
        
        return check(root.left,root.right)
    
        