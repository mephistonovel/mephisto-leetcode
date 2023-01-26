class Solution:
    def longestValidParentheses(self, s: str) -> int:
    # Longest Valid Parentheses

    # Solution 1 : Dynamic Programming
    #s = ")()())"
        if not s:
            return 0
        candidates = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    candidates[i] = (candidates[i-2] if i-2>=0 else 0) + 2
                elif s[i-1] == ')' and i - candidates[i-1] - 1 >=0 and s[i-candidates[i-1]-1] == '(':
                    candidates[i] = candidates[i-1] + 2 + (candidates[i - candidates[i-1] - 2] if i - candidates[i-1] - 2 >=0 else 0)
        return max(candidates)
        
        
#         if not s:
#             return 0
        
#         stack = []
#         stack.append(-1)
#         max_val = 0
        
#         for i in range(len(s)):
#             char = s[i]
#             if char == '(':
#                 stack.append(i)
#             else:
#                 stack.pop()
#                 if stack:
#                     max_val = max(max_val,i-stack[-1])
#                 else:
#                     stack.append(i)
                
        
#         return max_val
            

                
                
            
            
            
            
            
            