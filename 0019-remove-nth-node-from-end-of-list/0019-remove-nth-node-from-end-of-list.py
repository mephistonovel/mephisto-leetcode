# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = ListNode(0,head)
        curr = ans.next
        
        if (not curr.next):
            return None
        
        
        ## n 이 2이면 
        ## curr.next == None 일 때 해당 curr를 없애야 하고
        ## n=3: curr.next.next == None 일때 해당 curr을 없애야 하고
        ## n=k -> curr.next.next.......next (next (k-1)개) 일 때 해당 curr을 없애야 한다. 
        
        # i = 0 to final len
        
        # if n>len/2: len-n의 애를 끊고...
        # if n<len/2: len-n의애를 끊고.... or 
        
        length = 0
        while curr: 
            curr= curr.next
            length+=1
        
        print(length)
        
        stop_pos = length - n
        print(stop_pos)
    
        
        curr = ans.next
        pos = 0
        
        if n==1:
            while curr:
                if pos == stop_pos -1:
                    curr.next = None
                    break
                    
                curr = curr.next
                pos+=1
        
        else:
            while curr:
                if pos == stop_pos:
                    tmp = curr.next.val if curr.next else None
                    tmp_n = curr.next.next 
                    curr.val = tmp
                    curr.next = tmp_n
                    break


                curr = curr.next
                pos+=1

        
        return ans.next
                
        