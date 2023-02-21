# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None 

        #https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36977/My-short-post-order-traversal-Java-solution-for-share
        # Post order 변형
        # 원래는 342 -> 65 -> 1
        # 지금은 65-> 432 -> 1 
        
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
        
        
        ###https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/2672315/C%2B%2B-Solution-oror-Flatten-Binary-Tree-to-Linked-List
    
#         curr = root
        
#         while curr:
#             if curr.left:
#                 pred = curr.left
#                 while pred.right:
#                     pred = pred.right
                
#                 pred.right = curr.right 
#                 curr.right = curr.left
#                 curr.left = None
            
#             curr = curr.right
            
                
                
                
