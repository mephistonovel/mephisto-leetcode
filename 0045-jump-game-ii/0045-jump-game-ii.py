class Solution:
    def jump(self, nums: List[int]) -> int:
        #dp take the jump or not
        @lru_cache(maxsize = None)
        def dp(index):
            if(index >= len(nums)-1):
                return 0
            maxval = float("inf")
            for i in range(1, nums[index]+1):
                maxval = min(maxval, 1 + dp(index + i))
            return maxval
        return dp(0)

    ### time limit ###
#     from functools import lru_cache
#     def jump(self, nums: List[int]) -> int:
#         length = len(nums)
#         # goal = length -1 
        
#         # minval=len(nums)
#         last = len(nums)-1
#         ans = []
        
#         @lru_cache(maxsize = None) 
#         def dfs(index,count):
#             # print(count)
            
#             if index == last:
#                 ans.append(count)
#                 return 
            
#             # minval = float("inf")
#             jump_max = nums[index] if index < length else 0
#             for i in range(jump_max,0,-1):
#                 dfs(index+i,count+1)
                
        
#         dfs(0,0)
#         # print(ans)
#         return min(ans)
                