class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        fullen = len(''.join(words))
        each_len = len(words[0])
        # num_word = len(words)
        ls = (Counter(words))
    
        
        # fullen만큼의 길이를 s에서 찾아내야 함 
        l=0
        r=l+fullen
        
        window = Counter()
        ans = []
        
        while l<len(s) and r<=len(s):
            # cand = s[l:r]
            # print(s[l:r])
            # print(l)
            i=l
            while i<r:
                string = s[i:i+each_len]
                if string in ls:
                    window[string] = window.get(string,0)+1
                i+= each_len
            # print(len(window))
            # print('window',window)
            # # print(len(ls))
            # print('ls',ls)
            # print(ls-window)
            
            if len(window.keys()) == len(ls.keys()):
                # print(l, ls, window)
                window.subtract(ls)
                
                if set(window.values()) == {0}:
                    ans.append(l)
                    l+=1 
                    r+=1     
                else: 
                    l+=1
                    r+=1
            else:
                l+=1 
                r+=1 
            
            window = Counter()
        
        return ans 
                
            
            
                
            
            
                    
            
        