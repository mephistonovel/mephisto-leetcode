# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        ans = set()
        val = 0
        def dfs(r,val):
            if not r.left and not r.right:
                ans.add(val)
                return
            
            
            if r.left:
                dfs(r.left,val+r.left.val)
            if r.right:
                dfs(r.right,val+r.right.val)
        
        dfs(root,root.val)
        
        return targetSum in ans
        