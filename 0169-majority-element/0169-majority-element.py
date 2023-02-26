class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums.sort()
        std = len(nums)//2 # 양수에서는 floor기능 가능
        
        i=1
        tmp = nums[0]
        print(nums)
        for l in range(1,len(nums)):
            
            if nums[l]!= tmp:
                i=1
            else:
                i+=1
            
            # print(i,nums[l])
            if i>std:
                tmp = nums[l]
                break
            
            tmp = nums[l]
        
        return tmp

            
            
        