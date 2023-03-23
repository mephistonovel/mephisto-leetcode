class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        visited = set()
        end = len(graph)-1
        def dfs(node, path):
            visited.add(node)
            path.append(node)

            if node == end:
                paths.append(path[:])
            else:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dfs(neighbor, path)

            visited.remove(node)
            path.pop()

        dfs(0, [])
        return paths
#         ans = []
#         des = len(graph)-1
#         def dfs(node,path):
#             if node == des:
#                 ans.append(path[:])

#             for neighbor in graph[node]:
#                 path.append(neighbor)
#                 dfs(neighbor,path)
#                 path.pop()

         
#         dfs(0,[0])
#         return ans
