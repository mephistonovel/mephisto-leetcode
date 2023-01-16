class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dfsol(open,close,st,ans):
            if (open==0 and close ==0):
                ans.append(st)
                return
            
            if open>0:
                dfsol(open-1,close,st+"(",ans)
            
            if open<close:
                dfsol(open,close-1,st+")",ans)
        
        
        dfsol(n,n,"",ans)
        
        return ans
        