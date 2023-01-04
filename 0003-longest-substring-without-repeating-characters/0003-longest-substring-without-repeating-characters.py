class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointers 사용 : l, r
        l=0 #left pointer
#        r=0 #right pointer
        ans = {}
        maxval = 0
        
        for r in range(len(s)):
            ans[s[r]] = ans.get(s[r],0)+1 
            
            # 중복 발생 
            while ans[s[r]]>1:
                ans[s[l]] -= 1 # 원래 있던 애는 이제 옮겨 가니까 뺀다? 
                l +=1 
            
            maxval = max(maxval,r-l+1)
        
        return maxval

        
        
        
        
# 5%짜리 답안 
#         if len(s) == 0:
#             return 0
#         else:
#             init = 0
#             tmp = []
#             lengths = []
#             full_length = len(s)
#             while (init<full_length):
#                 char = s[init]
#                 if char not in tmp:
#                     tmp.append(char)
                    
#                 mediate_init = init+1 

#                 while mediate_init<full_length:
#                     char2 = s[mediate_init] 
#                     if char2 not in tmp:
#                         tmp.append(char2)
#                     else:
#                         print('tmp',tmp)

#                         length = len(tmp) 
#                         lengths.append(length)
#                         tmp = []
#                         break
                        
#                     mediate_init +=1 
                        
#                 init += 1 
                
#             lengths.append(len(tmp))
#             print('lengths',lengths)
            
#             return max(lengths) if len(lengths)>0 else 1 
        