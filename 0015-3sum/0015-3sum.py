class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        record =set()
        i=0
        nums = sorted(nums)
        while i<len(nums):
            cand = nums[i]
            if (nums[i]>0):
                break
            if (i>0) and (nums[i]==nums[i-1]):
                i+=1
                continue
            # if cand not in record:
                # rest1 = 0-cand
                
            next = i+1
            high = len(nums)-1

            while next<high:
                sum = cand+nums[next]+nums[high]
                if (sum>0):
                    high -=1
                elif (sum<0):
                    next +=1
                else:
                    candidate = [cand,nums[next],nums[high] ]
                    ans.append(candidate)
                    record.update(candidate)      

                    low_standard = nums[next]
                    high_standard = nums[high]
                    while (next<high) and (nums[next] == low_standard):
                        next +=1
                    while (next<high) and (nums[high] == high_standard):
                        high -=1 
                        
            i+=1
        
        return ans
                    
                
                
                
                