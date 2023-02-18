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
        
        
        ans = {targetSum:[]}
        # vals = []
        
        def dfs(node,tmp):
            # print(tmp)
            if not node.left and not node.right:
                # print(tmp)
                if sum(tmp[:]) == targetSum:
                    ans[targetSum].append(tmp[:])
                
                # vals.append(val)
                return
            
            if node.left:
                dfs(node.left,tmp+[node.left.val])
                
            if node.right:
                dfs(node.right,tmp+[node.right.val])
            
            tmp = tmp[:-1] # 하...이게 늘 포인트지 dfs의
        
        dfs(root,[root.val])
        
        return ans[targetSum]
        
        