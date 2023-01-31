class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        def dfs(rest,tmp):
            if len(tmp)==length:
                ans.append(tmp[:]) # [:]을 해야 다 복사된 채로 append가 된다...왜? 
                return 
            
            for num in rest:
                tmp.append(num)
                new_rest = list(set(nums)-set(tmp))
                dfs(new_rest,tmp)
                tmp.pop()
        
        dfs(nums,[])
        
        return ans
        