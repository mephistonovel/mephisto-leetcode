# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None and list2 == None:
            return None
        
        ans = ListNode(0,None)
        pos = ans 
        while list1 and list2:
            if list1.val<list2.val:
                pos.val = list1.val
                pos.next = ListNode()
                list1 = list1.next
            else:
                pos.val = list2.val
                pos.next = ListNode()
                list2 = list2.next
                
            pos = pos.next 
        
        if list1:
            pos.val = list1.val
            pos.next = list1.next
        
        if list2:
            pos.val = list2.val
            pos.next = list2.next 
        
        return ans
        
        