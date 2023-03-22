class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a=='0':
            return b
        if b=='0':
            return a
        
        
        def xor(v,u):
            return (v or u) and (not (v and u))
        
        if len(a)<len(b):
            a = "0"*(len(b)-len(a))+a
        elif len(a)>len(b):
            b = "0"*(len(a)-len(b))+b
        
        ans = ""
        tmp = 0
        
        for i,j in zip(a[::-1],b[::-1]):
            a1=bool(int(i))
            b1 =bool(int(j))
            res = xor(xor(a1,b1),tmp)
            
            ans+=str(int(res))
            if a1+b1+tmp>=2:
                tmp=1
            else:
                tmp=0
        
        if tmp==1:
            ans+="1"
            
        return ans[::-1]
            
            
#         n = len(a)
#         ans = ''
#         tmp = 0
#         for i in range(n):
      
                    