class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if min(nums)>1 or max(nums)<1:
            return 1
        nums = list(set(nums))
        nums.sort()
        mid = 0
        
        for i in range(len(nums)):
            if nums[i]>0:
                mid = i
                break       
                
        return self.check(nums[mid:])
            
    def check(self,positives):
        if positives[0]>1:
            return 1
        else:
            if len(positives)==1:
                return 2
            elif positives[1]-positives[0]>1:
                return 2
            else:
                i=1
                while i<len(positives) and (positives[i]-positives[i-1] == 1):
                    i+=1 
           
                return positives[i-1]+1
        