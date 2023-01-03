# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        s=0
        ans = ListNode(0,ListNode())
        pos = ans
        check_for_l1 = 0
        check_for_l2 = 0
        
        while (l1 or l2):
            num1 = 0 if l1 == None else l1.val
            num2 = 0 if l2 == None else l2.val
            cval = num1+num2+s 
            
            if l1==None:
                check_for_l1 = 2
            else:
                if l1.next==None:
                    check_for_l1 = 1
            if l2==None:
                check_for_l2 = 2
            else:
                if l2.next==None:
                    check_for_l2 = 1
                    
            print(check_for_l1)
            print(check_for_l2)

                    
            # if ((l1.next==None) and (l2.next == None)):
            print(cval)
            
            # 마지막 자리수
            if (check_for_l1 >=1 and check_for_l2 >= 1):
                if cval>=10:
                    cval = cval-10
                    s=1
                    
                    tmp = pos.next
                    tmp.val = cval
                    pos.next.next = ListNode(1,None)
                    pos = pos.next
                else:
                    s=0
                    tmp = pos.next
                    tmp.val = cval
                    pos = pos.next
            #마지막 자리수가 아닐 때    
            else:
                if cval>=10:
                    cval = cval-10
                    s=1
                else:
                    # cval = cval+s
                    s=0

                tmp = pos.next
                tmp.val = cval
                pos.next.next = ListNode()
                pos = pos.next
            
            
            if l1==None:
                l1 = None
            else:
                if l1.next==None:
                    l1=None
                else:
                    l1=l1.next 
                    
            if l2==None:
                l2 = None
            else:
                if l2.next==None:
                    l2=None
                else:
                    l2=l2.next 

        
        return ans.next
            
                
#         a1=[]
#         a2=[]
        
        
#         while (l1):
#             a1.append(l1.val)
#             l1 = l1.next
#         while l2:
#             a2.append(l2.val)
#             l2=l2.next
#         # a1, a2에 l1,l2의 문자들이 쌓임
        
        

#         check = 0
        
#         len1 = len(a1)
#         len2 = len(a2)
#         if len1>len2:
#             check=0
#         else:
#             check=1
        

            
#         #올림
#         s=0
        
        
#         #a1, a2에서 pop하여 더해 ans의 val로 넣기
#         #단, list가 차있을 때까지         
#         a1_len = len(a1)
#         a2_len = len(a2)
#         final_len=0
        
#         answer=[]
#         print('a1',a1)
#         print('a2',a2)
        
#         while ((final_len < a1_len) and (final_len<a2_len)):
#             num1 = a1.pop()
#             num2 = a2.pop()
#             cval = num1+num2
#             print(cval)
            
            
#             if cval>=10:
#                 answer.append(cval-10+s)
#                 s=1
#             else:
#                 answer.append(cval+s)
#                 s=0
                
#             final_len+=1
        

#         while (len(a1)!=0):
#             # if (final_len<a1_len):
#             if (len(a1)!=1):
#                 if (s==0):
#                     answer.append(a1.pop())
#                 else:
#                     k=a1.pop()
#                     if (k+s)>=10:
#                         answer.append(k+s-10)
#                         s=1
#                     else:
#                         answer.append(k+s)
#                         s=0
#             else:
#                 if (s==0):
#                     answer.append(a1.pop())
#                 else:
#                     k=a1.pop()
#                     if (k+s)>=10:
#                         answer.append(k+s-10)
#                         s=1
#                         answer.append(1)
#                     else:
#                         answer.append(k+s)
#                         s=0
                

#         while (len(a2)!=0):
#             if (s==0):
#                 answer.append(a2.pop())
#             else:
#                 answer.append(a2.pop()+1)
#                 s=0
        
        
#         if check==1:
#             if (len(answer)>len2):
#                 ans = ListNode(0,next=ListNode(answer[0],None))
#             else:
#                 ans = ListNode(0,next=ListNode())
#         else:
#             if (len(answer)>len1):
#                 ans = ListNode(0,next=ListNode(answer[0],None))
#             else:
#                 ans = ListNode(0,next=ListNode())
            
#         pos = ans
#         print(answer)
#         for i in range(len(answer)):
#             print(i,pos.val)
#             if i != (len(answer)-1):
#                 tmp = pos.next
#                 tmp.val = answer[i]
#                 pos.next.next = ListNode()
#                 pos = pos.next           
#             else:
#                 tmp = pos.next
#                 tmp.val = answer[i]
#                 # pos.next.next = ListNode()
#                 pos = pos.next 
                
            
            
        
#         return ans.next
        