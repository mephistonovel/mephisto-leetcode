# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(node,tmp):
            print(tmp)
            if not node.left and not node.right:
                
                val = ''.join(tmp)
                ans.append(int(val))
                return 
            
            if node.left:
                val_str = str(node.left.val)
                dfs(node.left,tmp+[val_str])
            if node.right:
                val_str = str(node.right.val)
                dfs(node.right,tmp+[val_str])
            
            tmp.pop()
        
        val_stroot = str(root.val)
        print(ans)
        dfs(root,[val_stroot])
        
        return sum(ans)
        