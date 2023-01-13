class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) ==1:
        #     return False 
        
        
        
        brackets = {"(":")","{":"}","[":"]"}
        # reverse_brackets = {")":"(", "}":"{", "]":"["}
        # left = set( ["(", "{", "["] )
        valid = []
            

            
        
        for char in s[::-1]:
            if char in brackets.values():
                valid.append(char)
            elif valid and brackets[char] == valid[-1]:
                valid.pop()
            else:
                return False
        
        return valid == []
            
#             # print(reverse_brackets[char])
            
#             if (char in reverse_brackets):
#                 if (reverse_brackets[char] in valid.keys()):
#                     rev_char = reverse_brackets[char]
#                     print(rev_char)
#                     if s[i-1] in left-set(rev_char):
#                         return False
#                     else:
#                         if valid[rev_char] == rev_char:
#                             valid[rev_char] = ''
#                         else:
#                             return False
#                 else:   
#                     print('else')
#                     return False
        
#         check = set(valid.values())
#         print('valid',valid)
#         print('check',check)
#         print('lencheck',len(check))
        
#         if check=={''}:
#             return True
#         else: 
#             return False
        

                   
        