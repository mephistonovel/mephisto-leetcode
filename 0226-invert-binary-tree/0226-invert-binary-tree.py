# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = deque([root])
        while q:
            x = q.popleft()
            tmp = x.left
            # print('tmpval', tmp.val if tmp else tmp)
            # print('x.left',x.left.val if x.left else x.left)
            # print('x.right',x.right.val if x.right else x.right)
            x.left = x.right
            x.right = tmp
            # 즉, 미리 left,right를 바꿔놓고, 그 순서대로 q에 넣어서 계속
            # 자식들의 swap을 하면 됨
            if x.left: q.append(x.left)
            if x.right: q.append(x.right)
        return root