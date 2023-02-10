# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if (not root.left) and (not (root.right)):
            return [[root.val]]
            
        ans = []
        q = deque([root])
        tmp = []
        
        j=0
        while q:
            lenq = len(q)
            
            for i in range(lenq):
                x = q.popleft()
                
                tmp.append(x.val)                
           
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        
        
            if j%2 == 0:
                ans.append(tmp)
            else:
                ans.append(reversed(tmp))
            j+=1
            tmp = []

                    
            
        return ans

            
                
        