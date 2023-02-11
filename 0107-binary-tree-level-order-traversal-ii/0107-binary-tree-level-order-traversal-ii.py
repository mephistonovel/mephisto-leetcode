# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        
        q = deque([root])
        tmp = []
        ans = []
        
        while q:
            len_q = len(q)
            
            for i in range(len_q):
                x = q.popleft()
                tmp.append(x.val)
                
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            
            ans.append(tmp)
            tmp = []
        
        return ans[::-1]
        