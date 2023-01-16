# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        i = 0
        ans = ListNode(0,next = head)
        curr = ans.next
        evens = []
        if not curr:
            return None
#        if not curr.next:
 #           return curr
        
        
        while curr:
            if i%2 == 0:
                prev = curr.val
            else:
                evens.append(curr.val)
                curr.val = prev
            
            i+=1
            curr = curr.next
        
        curr = ans.next
        
        for i in range(len(evens)):
            curr.val = evens[i]
            curr = curr.next.next
        
        return ans.next
            
                
                
        
        