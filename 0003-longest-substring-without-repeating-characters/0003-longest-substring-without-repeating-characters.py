class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        if len(s) == 0:
            return 0
        else:
            init = 0
            tmp = []
            lengths = []
            full_length = len(s)
            while (init<full_length):
                char = s[init]
                if char not in tmp:
                    tmp.append(char)
                    
                mediate_init = init+1 

                while mediate_init<full_length:
                    char2 = s[mediate_init] 
                    if char2 not in tmp:
                        tmp.append(char2)
                    else:
                        print('tmp',tmp)

                        length = len(tmp) 
                        lengths.append(length)
                        tmp = []
                        break
                        
                    mediate_init +=1 
                        
                init += 1 
                
            lengths.append(len(tmp))
            print('lengths',lengths)
            
            return max(lengths) if len(lengths)>0 else 1 
            
            
        # else:
        #     lengths = [] # length 기록 
        #     tmp = [] # 임시 컨테이너 for 중복문자 확인 
        #     for char in s:
        #         if char not in tmp:
        #             tmp.append(char)
        #         else:
        #             print('tmp',tmp)
        #             length = len(tmp)
        #             lengths.append(length)
        #             # length기록 후 지우기 
        #             tmp=[]
        #             tmp.append(char)
        #     lengths.append(len(tmp))
        #     print('lenghts',lengths)
        #     return max(lengths) if len(lengths)>0 else 1
        
        
            
            
            
            
        
#             char = s[i]
#             if (char!=prev):
#                 if (char not in ans.keys()):
#                     ans[anchor]+=1
#                 else:
                    
#             else:
#                 if (char not in ans.keys()):
#                     anchor = char
#                     ans[anchor]=1
#                 else:
                    
            # if (char != prev):
            #     ans[char] +=1 
            # else:
            #     ans[char]=1
            # prev = char
        
#         return max(ans.values())
        