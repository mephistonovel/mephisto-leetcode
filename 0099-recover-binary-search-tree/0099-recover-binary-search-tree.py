# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # in order활용?
        change = set()
        def check(node):
            ans = []
            def dfs(node):
                # print(ans)
                if not node:
                    return
                else:
                    dfs(node.left)
                    ans.append(node.val)
                    dfs(node.right)                    
                    
            
            if node.left:
                ans = []
                dfs(node.left)
                # print(ans)
                if max(ans)>node.val:
                    change.add((node.val,max(ans)))
            if node.right:
                ans = []
                dfs(node.right)
                if min(ans)<node.val:
                    change.add((node.val,min(ans)))
                    
        
        q = deque([root])
        
        while q and not change:
            lenq = len(q)
            for i in range(lenq):
                x = q.popleft()
                check(x)
                
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        
        # print(change) #{(2,3),(2,1)}
        change = list(change)
        q2 = deque([root]) 
        if len(change) ==1:
            ch_pair = change[0]
        if len(change)>1:
            # if change[0][0] == change[1][0]:
            ch_pair = (change[0][1],change[1][1])
        while q2: 
            lenq = len(q2)
            for i in range(lenq):
                x = q2.popleft()
                if x.val in ch_pair:
                    x.val = list(set(ch_pair)-{x.val})[0]

                if x.left:
                    q2.append(x.left)
                if x.right:
                    q2.append(x.right)
                    
#         # def check(numbers,node_val):
#         root_index = ans.index(root.val)
#         left = ans[:root_index]
#         right = ans[root_index+1:]

#         if left and max(left)>root.val:
#             change_val = max(left)
#         if right and min(right)<root.val:
#             change_val = min(right)
            
#         # root.val = change_val
#         # print(change_val)
#         q = deque([root])
#         ch = True
        
#         while q and ch:
#             qlen = len(q)
#             for i in range(qlen):
#                 x = q.popleft() 
#                 if x.val == change_val:
#                     # print(1)
#                     x.val = root.val 
#                     ch = False 
#                     break
                
#                 if x.left:
#                     q.append(x.left)
#                 if x.right:
#                     q.append(x.right)
        
#         root.val = change_val
            
            
        
        