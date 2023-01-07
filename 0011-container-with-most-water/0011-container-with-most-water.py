class Solution:
    def maxArea(self, height: List[int]) -> int:
        init = 0 
        end = len(height)-1
        ans = 0
        while (init < end):
            size = (end-init)*min(height[init],height[end])
            if ans<size:
                ans = size
                
            if height[init]<height[end]:
                init+=1
            else:
                end-= 1
                
        return ans 
    
#         length = len(height)
#         ans = 0
#         for i in range(length):
#             end = i+1 # or i
#             for j in range(end,length):
#                 size = (j-i)*min(height[i],height[j])
#                 # print(size)
#                 ans = max(ans,size)
        
#         return ans