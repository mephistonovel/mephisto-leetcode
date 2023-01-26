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
        
        # [1,2,3,4,5]
        # k=3
        while curr:
            if i == k:
                # [ [1,2,3,4,5], [2,3,4,5] ] 
                new_cur = q.popleft() # [1,2,3,4,5]
            
                first = curr #처음으로 갈 거 받아놓기 # first [3,4,5]    

                new_cur.next = curr.next # 1-> 4 ->5
                curr = curr.next 
                
                tmp_cur = new_cur # [1 ->4]
                
                while q:
                    prev_cur = q.popleft() # [2,3,4,5]
                    prev_cur.next = tmp_cur # 2-> 1 ->4 -5
                    tmp_cur = prev_cur 
                
                
                first.next = tmp_cur # 3->2->1->4->5
                jump.next =first   # 0-> 3 -> 2->1->4->5얘가 문제네 ㅋㅋㅋㅋ
                
                jump = new_cur # 
                
                
                i=1
                
                
            else:                
                q.append(curr) # [ [1,2,3,4,5], [2,3,4,5] ] 
                curr = curr.next
                i+=1
        
        return ans.next 
        