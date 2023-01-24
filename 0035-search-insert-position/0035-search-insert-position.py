class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        init = 0
        end = len(nums)-1
        mid = end//2
        
        while init<=end:        
            m = nums[mid]
            
            if target>m:
                init = mid+1
                mid = init + (end-init)//2
            
            elif target<m:
                end = mid-1
                mid = init + (end-init)//2
            
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

        
            