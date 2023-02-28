class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        
        if len(nums)==4 and sum(nums)==target:
            return [nums]
        
        nums.sort()
### https://leetcode.com/problems/4sum/discuss/3116272/Easily-Understandable-solution-oror-Beats-99.30 ###
                         
    
        ans = []
        length = len(nums)
        for i in range(length-3):
            if i>0 and nums[i]==nums[i-1]: continue
            n0 = nums[i]
            for j in range(i+1,length-2):
                if j>i+1 and nums[j]==nums[j-1]: continue
                n1 = nums[j]    
                targ = target - n0-n1
                k = j+1 
                l = len(nums)-1
                
                while k<l:
                    if nums[k]+nums[l]<targ:
                        k+=1 
                    elif nums[k]+nums[l]>targ:
                        l-=1 
                    else:
                        ans.append([n0,n1,nums[k],nums[l]])
                    
                        low_ = nums[k]
                        high_ = nums[l]

                        while k<l and nums[k]==nums[k+1]:
                            k+=1
                        while k<l and nums[l]==nums[l-1]:
                            l-=1
                        k+=1
                        l-=1
                        
        
        return ans
        
        