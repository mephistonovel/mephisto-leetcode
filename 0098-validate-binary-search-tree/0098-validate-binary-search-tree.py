# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    isvalid = True 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        # isvalid = True
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if ans and root.val<=ans[-1]:
                self.isvalid = False 
            ans.append(root.val)
            dfs(root.right)

            return self.isvalid
        
        return dfs(root)
        
#         ans = []
#         def dfs(node):
#             if not node:
#                 return
#             dfs(node.left)
#             ans.append(node.val) 
#             dfs(node.right)
        
#         dfs(root)
#         for i in range(1,len(ans)):
#             if ans[i]<=ans[i-1]:
#                 return False 
        
#         return True
        