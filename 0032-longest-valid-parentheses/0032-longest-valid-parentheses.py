class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        # ans = 0
        # pair = {'(':')'}
        stack.append(-1)
        max_val = 0
        
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_val = max(max_val,i-stack[-1])
                else:
                    stack.append(i)
                
        
        return max_val
            

                
                
            
            
            
            
            
            

            
        return max_val 
                
                
#         def pair_valid(s,ans):
#             pair = '()'
#             # print(s)
#             print(ans)
#             if pair in s:
#                 origin = len(s)
#                 new = len(s.replace(pair,''))
#                 reduce = origin-new
#                 # print(reduce)
                
#                 return pair_valid(s.replace(pair,''),ans+reduce)
#             else: 
#                 return ans
        
        # return pair_valid(s,ans)
            
                
        
        
        