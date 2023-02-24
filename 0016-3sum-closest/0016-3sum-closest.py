class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)==3:
            return sum(nums)
        
        nums.sort()
        dif = dict()
        for l in range(len(nums)-2):
            n0 = nums[l]
            targ = target-nums[l]
            i1 = l+1
            i2 = len(nums)-1
            cand = n0+ nums[i1]+nums[i2]
            
            while i1<i2:
                cand = n0+nums[i1]+nums[i2]
                dif[abs(target-cand)] = cand
                if nums[i1]+nums[i2] == targ:
                    return targ+n0
                elif nums[i1]+nums[i2]<targ:
                    i1+=1 
                else:
                    i2-=1 
                
            
        print(dif)
        
        return dif[sorted(list(dif.keys()))[0]]
            
            
                    
            
                
        
        