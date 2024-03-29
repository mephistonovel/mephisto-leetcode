# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxdep = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node,dep):
            if not node.left and not node.right:
                self.maxdep = max(dep,self.maxdep)
            
            if node.left:
                dfs(node.left,dep+1)
            if node.right:
                dfs(node.right,dep+1)
        
        dfs(root,1)
        return self.maxdep