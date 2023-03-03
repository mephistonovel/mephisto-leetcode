# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans =[]
        q = deque([root])
        while q:
            lenq = len(q)
            tmp = []
            for i in range(lenq):
                x = q.popleft()
                tmp.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

                if i == lenq-1:
                    ans.append(tmp)
                    tmp = []
        
        return ans
