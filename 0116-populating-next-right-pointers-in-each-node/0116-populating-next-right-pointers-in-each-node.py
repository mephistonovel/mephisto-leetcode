"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        vis_node = deque()
        vis_node.appendleft(root)
        
        i = 1
        j=0
        
        
        while vis_node:
            x = vis_node.popleft()
            
            if i==2**j: 
                x.next = None 
                i=0
                j+=1 
            else:
                x.next = vis_node[0]
                
                
            if x.left and x.right:
                vis_node.append(x.left)
                vis_node.append(x.right)
            i+=1
        
        return root
        