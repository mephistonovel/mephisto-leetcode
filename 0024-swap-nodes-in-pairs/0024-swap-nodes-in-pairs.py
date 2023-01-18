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
        if not curr.next:
            return curr
        
        
        while curr:
            if i%2 == 0:
                prev = curr.val
            else:
                evens.append(curr.val)
                curr.val = prev
            
            i+=1
            curr = curr.next
        
        curr = ans.next
        
        for j in range(len(evens)):
            curr.val = evens[j]
            curr = curr.next.next
        
        return ans.next
    
    # Definition for singly-linked list.
    
##################     
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def swapPairs(self, head:ListNode) -> ListNode:
        if not head or not head.next:
            return head
        start=front = ListNode(None)
        front.next = head
        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = head
            front.next = temp
            head = head.next
            front= front.next.next
        return start.next

 ##################
                
                
        
        
