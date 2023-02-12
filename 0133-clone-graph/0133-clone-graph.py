"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        ### https://leetcode.com/problems/clone-graph/discuss/1793212/C%2B%2Bor-Detailed-Explanation-w-DFS-and-BFS-or-Commented-code-with-extra-Test-Case ### 
        
        # print(node.neighbors)
        new_node = Node(val=node.val,neighbors=[])
        
        q = deque([node])
        # newq = deque([new_node])
        visited = dict()
        visited[node] = new_node # 
        
        while q:

            x = q.popleft()

            for n in x.neighbors:
                if n not in visited:
                    q.append(n)
                    visited[n] = Node(val=n.val, neighbors = [])
                    
                visited[x].neighbors.append(visited[n])

        return new_node
                        
            
            
        