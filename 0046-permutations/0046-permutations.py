class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        def dfs(rest,tmp):
            if len(tmp)==length:
                ans.append(tmp[:])
                return 
            
            for num in rest:
                tmp.append(num)
                new_rest = set(nums)-set(tmp)
                new_rest = list(new_rest)
                dfs(new_rest,tmp)
                tmp.pop()
        
        dfs(nums,[])
        
        return ans
        