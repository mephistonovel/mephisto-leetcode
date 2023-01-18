# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1 or set(lists) == {None}:
            return lists[0]
        if len(lists) == 1 and lists[0] == None:
            return None
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node=node.next
        
        values.sort(reverse=True)
        
        ans = curr = ListNode()
        
        while values:
            if len(values) ==1:
                curr.val = values.pop()
                continue 
            curr.val = values.pop()
            curr.next = ListNode()
            curr=curr.next
        
        return ans
            
#https://leetcode.com/problems/merge-k-sorted-lists/discuss/2878522/Divide-and-conquer-solution-python#
        
        
        
############ time over 풀이 ########
#         if not lists:
#             return None
#         if len(lists) == 1 or set(lists) == {None}:
#             return lists[0]
#         if len(lists) == 1 and lists[0] == None:
#             return None
        
#         from numpy import array,argmin
        
        
    
    
#         ans = ListNode()
#         pos = ans
#         k = len(lists) # lists안에 있는 linked list 개수
        
#         while set(lists) != {None}:
#             cand = []
#             for i in range(k):
#                 curr = lists[i]
#                 if not curr:
#                     cand.append(10001)
#                     continue 
#                 cand.append(curr.val)
            
#             print(cand)
#             loc = argmin(array(cand))
#             print(loc)
#             if (not lists[loc].next) and (set(lists) == {None,lists[loc]}):
#                 pos.val = lists[loc].val
#             else:
#         # 마지막인 걸 어떻게 알까? 
#                 pos.val = lists[loc].val
#                 pos.next = ListNode()
#                 pos = pos.next

#             # 빠진 애는 아예 listnode 우측으로 움직여주기
#             if lists[loc].next:
#                 tmp_val = lists[loc].next.val
#                 lists[loc].val = tmp_val
#                 lists[loc].next = lists[loc].next.next
#             else:
#                 lists[loc] = None
        
#         pos = None
        
        
        
#         return ans
