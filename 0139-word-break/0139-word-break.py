class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sl=list(s)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        # dp = [i==0 for i in range(n+1)]
        # print(dp)
        
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break 
        return dp[-1]
        
        
        