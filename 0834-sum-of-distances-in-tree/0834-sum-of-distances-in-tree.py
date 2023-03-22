class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * n
        ans = [0] * n
        def dfs(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + n - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans
#         visited = [False]*n
#         pd = dict()
#         adj = defaultdict(list)
#         for a,b in edges:
#             adj[a].append(b)
#             adj[b].append(a)
        # while q:
        #     x = q.popleft()
        #     for neighbor in adj[x]:
        #         if not visited[neighbor]:
        #             q.append(neighbor)
        #             visited[neighbor]=True
        #             pd[neighbor] = (x,pd[x][1]+1)
        #             zero+=pd[x][1]+1
        
        
        
        ### 플로이드 와샬 ### time limit
#         adjmat = [[float('inf') for i in range(n)] for j in range(n)]
#         for i in range(n):
#             adjmat[i][i] = 0
            
#         for a,b in edges:
#             adjmat[a][b] = 1
#             adjmat[b][a] = 1
#         for k in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     if i==j:
#                         continue
#                     if adjmat[i][k]+adjmat[k][j]<adjmat[i][j]:
#                         adjmat[i][j]=adjmat[i][k]+adjmat[k][j]
                
#         ans = []
#         for i in range(n):
#             ans.append(sum(adjmat[i]))
        
#         q = deque([0])
#         visited[0]=True
#         pd[0] = (-1,0)
#         ans = []
#         zero=0
        
        

        
        
        return ans
        