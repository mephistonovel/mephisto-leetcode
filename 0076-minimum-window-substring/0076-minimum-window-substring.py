class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ########## https://leetcode.com/problems/minimum-window-substring/discuss/2732034/Easy-Approach-with-Explanation%3A-97.81-faster-than-others #############
        if t=="" or len(t) > len(s):
            return ""
    
        res, reslen = [-1,-1], float("inf")
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)

        window = {}
        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in countT and window[ch] == countT[ch]:
                have += 1

            while have == need:
                if (r-l+1) < reslen:
                    res = [l, r]
                    reslen = r-l+1

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1

        l,r = res
        return s[l:r+1] if reslen != float("inf") else ""
        
#         if len(t)>len(s):
#             return ""
        
#         ind = dict()
#         # print(t in s)
        
#         jump = len(t)
#         ans_l = 0
#         ans_r = 0
#         check = dict()
#         set_t = set(t)
#         leng = 0
        
#         def find(l,r,val):
            
#             while l<r and l>0 and r<len(s) and (not check.values() or (set(check.values())) != {1}):
#                 print(check)
#                 tmp = s[l:r]
#                 for i in range(jump):
#                     char = t[i]
#                     if char in tmp:
#                         check[i] = 1
#                     else:
#                         check[i]=0
                
#                 val = r-l+1
#                 l-=1
#                 r+=1
                
#             return l+1, r,val
        
        
#         for k in range(len(s)):
#             left, right, new_len = find(k,k+1,0)
#             print('l,r,n',left, right,new_len)
            
#             if new_len<leng:
#                 leng = new_len
#                 ans_l = left
#                 ans_r = right
        
#         return s[ans_l:ans_r]
                
                
 
            
            
            
                    
            