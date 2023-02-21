# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


### two pointer +inorder ### https://leetcode.com/problems/recover-binary-search-tree/discuss/1962281/C%2B%2B-oror-Easy-to-understand
#inorder는  sorting한 배열을 뱉어주니까...sort에서 틀린값이 있다면 해당 값들만 change! 
class Solution:
    def __init__(self):
        self.first = None   
        self.second = None
        self.pre = TreeNode(-2**31-1)
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val 
        
    def dfs(self, node):
        if not node:
            return
        else:
            self.dfs(node.left)
            if self.first == None and node.val<self.pre.val:
                self.first = self.pre
            if self.first != None and node.val<self.pre.val:
                self.second = node
            self.pre = node

            self.dfs(node.right)

        

#############15%defeat##########
#         change = set()
#         def check(node):
#             ans = []
#             def dfs(node):
#                 # print(ans)
#                 if not node:
#                     return
#                 else:
#                     dfs(node.left)
#                     ans.append(node.val)
#                     dfs(node.right)                    
                    
            
#             if node.left:
#                 ans = []
#                 dfs(node.left)
#                 # print(ans)
#                 if max(ans)>node.val:
#                     change.add((node.val,max(ans)))
#             if node.right:
#                 ans = []
#                 dfs(node.right)
#                 if min(ans)<node.val:
#                     change.add((node.val,min(ans)))
                    
        
#         q = deque([root])
        
#         while q and not change:
#             lenq = len(q)
#             for i in range(lenq):
#                 x = q.popleft()
#                 check(x)
                
#                 if x.left:
#                     q.append(x.left)
#                 if x.right:
#                     q.append(x.right)
        
#         # print(change) #{(2,3),(2,1)}
#         change = list(change)
#         q2 = deque([root]) 
#         if len(change) ==1:
#             ch_pair = change[0]
#         if len(change)>1:
#             # if change[0][0] == change[1][0]:
#             ch_pair = (change[0][1],change[1][1])
#         while q2: 
#             lenq = len(q2)
#             for i in range(lenq):
#                 x = q2.popleft()
#                 if x.val in ch_pair:
#                     x.val = list(set(ch_pair)-{x.val})[0]

#                 if x.left:
#                     q2.append(x.left)
#                 if x.right:
#                     q2.append(x.right)
                    

            
        
        