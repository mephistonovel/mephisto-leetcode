# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.ans = TreeNode()
    #     self.tmp = self.ans
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None 
        
        curr = root
        
        while curr:
            if curr.left:
                pred = curr.left
                while pred.right:
                    pred = pred.right
                
                pred.right = curr.right 
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right
            
                
                
                
#         for val in ans:
#             # print(ans_node)
#             tmp_node.val = val
#             tmp_node.right = TreeNode()
#             tmp_node = tmp_node.right
            
#         root = ans_node
#         print(root)
        