class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        init = 0
        end = len(nums)-1
        mid = end//2
        check = 0
        
        while init<=end:            
#             s = nums[init]
#             e = nums[end]
            m = nums[mid]
            
            if target>m:
                init = mid+1
                mid = init + (end-init)//2
                check = 1
            
            elif target<m:
                end = mid-1
                mid = init + (end-init)//2
                check = 0
            
            else:
                return mid 
            

        
        # 이 예외처리가 ㅋㅋㅋ
        if mid==-1:
            return 0
        
        #일반        
        if nums[mid]>target:
            return mid     
        else:
            return mid+1
        
            
        
        # if mid == 0 and check:
        #     return mid+1
        # elif mid == 0 and (not check):
        #     return mid
        # elif (mid == len(nums)-1) and check:
        #     return len(nums)
        # elif (mid == len(nums)-1) and (not check):
        #     return mid
        # elif not check:
        #     return mid+1
        # else:
        #     return mid
        
        
            