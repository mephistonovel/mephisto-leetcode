# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = []
        def dfs(node,dep):
            if not node.left and not node.right:
                ans.append(dep)
            
            if node.left:
                dfs(node.left,dep+1)
            if node.right:
                dfs(node.right,dep+1)
        
        dfs(root,1)
        return max(ans)