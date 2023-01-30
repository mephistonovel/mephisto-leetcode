from functools import lru_cache
class Solution:
###https://leetcode.com/problems/jump-game-ii/discuss/3106089/five-lines-(9ms)-C%2B%2B-Solutions-(Beats-97.10)###
    def jump(self,nums: List[int]) -> int:
        pos = des = 0
        count = 0
        for i in range(0,len(nums)-1):
            des = max(des,nums[i]+i)
            if (pos==i):
                pos = des
                count+=1
        
        if pos>=(len(nums)-1):
            return count
        return -1

### DP solution ### 
    # def jump(self, nums: List[int]) -> int:
    #     #dp take the jump or not
    #     @lru_cache(maxsize = None)
    #     def dp(index):
    #         if(index >= len(nums)-1):
    #             return 0
    #         maxval = float("inf")
    #         for i in range(1, nums[index]+1):
    #             maxval = min(maxval, 1 + dp(index + i))
    #         return maxval
    #     return dp(0)

    ### time limit ###
#     from functools import lru_cache
#     def jump(self, nums: List[int]) -> int:
#         length = len(nums)
#         last = len(nums)-1
#         ans = []
        
#         @lru_cache(maxsize = None) 
#         def dfs(index,count):
         
#             if index >= last:
#                 ans.append(count)
#                 return 
            
#             jump_max = nums[index] if index < length else 0
#             for i in range(jump_max,0,-1):
#                 dfs(index+i,count+1)
                
        
#         dfs(0,0)
#         # print(ans)
#         return min(ans)
                