# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        
        # ans = {targetSum:[]}
        # vals = []
        ank = []
        
        def dfs(node,tmp,val):
            if not node.left and not node.right:
                if val == targetSum:
                    ank.append(tmp[:])
                # if sum(tmp[:]) == targetSum:
                #     ans[targetSum].append(tmp[:])
                return
            
            if node.left:
                dfs(node.left,tmp+[node.left.val],val+node.left.val)
                
            if node.right:
                dfs(node.right,tmp+[node.right.val],val+node.right.val)
            
            tmp = tmp[:-1] # 하...이게 늘 포인트지 dfs의
        
        dfs(root,[root.val],root.val)
        
        return ank
        
        