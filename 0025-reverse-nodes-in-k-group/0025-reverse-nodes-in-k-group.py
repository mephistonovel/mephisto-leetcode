# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        q = deque()
        i=1
        ans = jump = ListNode(0,next=head)
        
        if k==1:
            return ans.next 
        
        curr = ans.next
        
        while curr:
            if i == k:
                new_cur = final = q.popleft()
            
                first = curr #처음으로 갈 거 받아놓기    

                final.next = curr.next
                curr = curr.next
                
                tmp_cur = new_cur
                
                while q:
                    prev_cur = q.popleft()
                    prev_cur.next = tmp_cur
                    tmp_cur = prev_cur
                
                
                first.next = tmp_cur
                jump.next =first   #얘가 문제네 ㅋㅋㅋㅋ
                
                jump = new_cur
                
                
                i=1
                
                
            else:                
                q.append(curr)
                curr = curr.next
                i+=1
        
        return ans.next 
        