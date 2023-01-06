class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(s,l,r):
            while ((l>=0) and (r<len(s)) and (s[l]==s[r])):
                l-=1
                r+=1 
            return r-(l+1), l+1
        
        if len(s) <= 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        else:
            length = 0
            for i in range(len(s)):
                len1,l1 = check(s,i,i)
                len2,l2 = check(s,i,i+1)
                
                len_i = max(len1,len2)
                
                if length<len_i:
                    length = len_i
                    if len_i == len1:
                        left =l1
                    else: 
                        left = l2
                        

            return s[left:left+length]
                    
        
