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
            
        queue,degrees = [],{}
        for node, neighbors in adj.items():
            degrees[node] = len(neighbors)
            # Insert all leaves into our priority queue.
            if degrees[node] == 1:
                queue.append(node)
        ans = []
        while queue:
            nodes = []
            while queue:
                nodes.append(queue.pop())
            ans = nodes
            for node in nodes:
                degrees[node] -= 1
                for neighbor in adj[node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)
        return ans
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
        
            
        
        