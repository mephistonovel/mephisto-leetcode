# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ### https://otugi.tistory.com/264 ### 
        if not head or not head.next:
            return head
        
        p, slow, fast = None, head, head
        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
        p.next = None
        
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self,n1,n2):
        final = ans = ListNode(0,None)
        
        while n1 and n2:
            if n1.val<=n2.val:
                # ans.val = n1.val
                # n1=n1.next
                ans.next,n1 = n1,n1.next
            else:
                # ans.val = n2.val
                # n2 = n2.next
                ans.next,n2 = n2,n2.next
            ans = ans.next
        
        if n1:
            # ans.val = n1.val
            # ans.next = n1.next
            ans.next = n1
        
        if n2:
            ans.next = n2
      
        
        return final.next
                
        
        
        
        
        #### selection sort는 timelimit #### 
#         # selection sort
#         # find_minimum for head[i:]
#         def find_min(node):
#             minval = 10**5+1
#             minnode = None
            
#             while node:
#                 if node.val<minval:
#                     minval = node.val
#                     minnode = node
                
#                 node = node.next 
                
#             return minnode
        
#         curr = head
        
#         #sort
#         while curr:
#             minnode = find_min(curr)
#             curr.val, minnode.val = minnode.val,curr.val
#             curr=curr.next
            
        
#         return head
            
        
            
            
        