class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        fullen = len(''.join(words))
        each_len = len(words[0])
        ls = (Counter(words))
    
        
        # fullen만큼의 길이를 s에서 찾아내야 함 
        l=0
        r=l+fullen
        
        window = Counter()
        ans = []
        
        while l<len(s) and r<=len(s):
            i=l
            while i<r:
                string = s[i:i+each_len]
                if string in ls:
                    window[string] = window.get(string,0)+1
                i+= each_len
            
            if len(window.keys()) == len(ls.keys()):
                window.subtract(ls) # counter는 각 counter끼리 빼주기 가능. 단 이거 자체는 method라 None 
                
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
                
            
            
                
            
            
                    
            
        