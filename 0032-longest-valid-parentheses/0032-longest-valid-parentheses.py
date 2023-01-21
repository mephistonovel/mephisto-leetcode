class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
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
            

                
                
            
            
            
            
            
            