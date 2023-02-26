class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ### no sorting ###
        
        check = dict()
        std = len(nums)//2
        
        for n in nums:
            if n not in check:
                check[n]=1
            else:
                check[n]+=1
        
        print(check)
        ans = 0
        for n,item in check.items():
            if item>std:
                ans = n
                break
        
        return ans
        
        
        
        
        ### sorting #### 
#         nums.sort()
#         std = len(nums)//2 # 양수에서는 floor기능 가능
        
#         i=1
#         tmp = nums[0]
    
#         for l in range(1,len(nums)):
            
#             if nums[l]!= tmp:
#                 i=1
#             else:
#                 i+=1
#             if i>std:
#                 tmp = nums[l]
#                 break
            
#             tmp = nums[l]
        
#         return tmp

            
            
        