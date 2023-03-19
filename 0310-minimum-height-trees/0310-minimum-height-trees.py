class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [n-1]
        if n==2:
            return edges[0]
    
        # https://leetcode.com/problems/minimum-height-trees/discuss/3240534/310%3A-Time-96.8-Solution-with-step-by-step-explanation
        # adjacency list
        adj = collections.defaultdict(set)
        for i,j in edges:
            adj[i].add(j)
            adj[j].add(i)
        
        # adj list에서 length가 1인건 무조건 리프
        leaves = [i for i in range(n) if len(adj[i])==1]
        
        while n>2:
            n-=len(leaves)
            new_l=[]
            for leaf in leaves:
                nei = adj[leaf].pop()
                adj[nei].remove(leaf)
                
                if len(adj[nei])==1:
                    new_l.append(nei)
            leaves = new_l
        return leaves
#         # dfs code
#         visited = [False]*n
#         ans=[]
#         def dfs(k,i):
#             if not visited[k]:
#                 visited[k] = True
#                 for w in adj[k]:
#                     dfs(w,i+1)
#             else:
#                 ans.append(i)
                
        
#         # distance dict
#         dist = collections.defaultdict(list)
        
#         for i in range(n):
#             visited = [False]*n
#             ans = []
#             dfs(i,-1)
#             # print(ans)
#             dist[max(ans)].append(i)
        
#         key = 0
#         for h in range(n):
#             if h in dist:
#                 key = h
#                 break
#         return dist[key]
        
            
        
        