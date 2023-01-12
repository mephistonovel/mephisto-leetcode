class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    ########### 답안 ##############
#         if digits == "":
#             return []
#         else:
#             res = []
#             dt = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
#         }
#             def helper(index,string):
#                 if index==len(digits):
#                     res.append(string)
#                     return True
#                 for ele in (dt[digits[index]]):
#                     string+=ele
#                     helper(index+1,string)
#                     string = string[:-1]
#             helper(0,"")    
            
#             return res
        
    ################################
    
    
            if len(digits) == 0:
                return []
            
            ans = []
            
            length = len(digits)
            visited = []
            # net = {}
            # net[digits[0]] = [*dg[digits[0]]]
            
            need_visited = deque()
            need_visited.extend('0') #'abc' -> ['a','b','c']
            i=0
            tmp = ''
            check = 1 
            check2 = 2
            dg = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
            
            def dfsol(index,tmp):
                if len(tmp) == length:
                    ans.append(tmp)
                    return True
                
                for char in dg[digits[index]]:
                    # print(tmp)
                    tmp += char
                    dfsol(index+1,tmp)
                    tmp = tmp[:-1]
            
            dfsol(0,"")
            
            return ans
            
            
            
#             while need_visited:
#                 print(need_visited)
                
#                 node = need_visited.pop()
#                 print(node)
                
                    
#                 if (node not in tmp) or check<=limit:
#                     # visited.append(node)
#                     tmp+=node
#                     if len(tmp) == length+1 and check <limit:
#                         print('1c',tmp)
#                         ans.append(tmp[1:])
#                         tmp = tmp[:-1]
#                         check+=1
#                         print('1c',tmp)
#                     elif len(tmp) == length+1 and check == limit:
#                         if check2<limit2:
#                             print('2c',tmp)

#                             ans.append(tmp[1:])
#                             for j in range(i+1):
#                                 tmp = tmp[:-1]
#                             # tmp = tmp[:-1]
#                             check=1
#                             check2+=2
#                             i-=1
#                             print('2c',tmp,i)
#                         else:
#                             ans.append(tmp[1:])
#                             for j in range(i+2):
#                                 tmp = tmp[:-1]
#                             # tmp = tmp[:-1]
#                             check=1
#                             # check2+=2
#                             i-=1
#                             print('2c',tmp,i)
                            
#                     else:
#                         need_visited.extend([*dg[digits[i]]])
#                         limit = len(dg[digits[i]]) # 3
#                         limit2 = len(dg[digits[i-1]])
#                         i+=1
#                 # else:
                #     tmp = tmp[:-1]
                #     i-=1
                # i+=1 
                
            
            return ans
            
            
            
        