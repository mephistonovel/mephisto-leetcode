class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        des = len(graph)-1
        def dfs(node,path):
            if node == des:
                ans.append(path[:])

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor,path)
                path.pop()

              # if neighbor.color == 'W':
              #   neighbor.color = 'R'
              
        # s.color = 'R'
        dfs(0,[0])
        return ans