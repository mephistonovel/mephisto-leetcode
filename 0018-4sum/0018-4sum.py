class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        if len(nums)==4 and sum(nums)==target:
            return [nums]
        
        nums.sort()
#         length = len(nums)
#         zero = dict()
#         zero[0] = 0
#         ans = []
        
#         for i in range(len(nums)):
#             if nums[i]==0:
#                 zero[0] +=1
                
#         print(zero[0])
#         num_zero=zero[0]
        
#         if num_zero>=3:
#             if target in nums:
#                 ans.append([target,0,0,0])
                
#         if num_zero>=2:
#             match = set()
            
#             for i in range(length):
#                 if nums[i]==0: continue
#                 if 0<i<length-1 and nums[i]==nums[i+1]: 
#                     if nums[i]*2 == target:
#                         tmp=nums[i]
#                         ans.append([0,0,tmp,tmp])
#                     continue 
#                 cur = nums[i]
#                 targ = target - cur
#                 if targ in match:
#                     ans.append([0,0,cur,targ])
#                 else:
#                     match.add(cur)
            
#         if num_zero>=1:
#             for i in range(length):
#                 if nums[i] == 0: continue
#                 cur = nums[i]
#                 targ = target-cur
#                 mat = set()
#                 for j in range(i+1,length):
#                     if nums[j]==0: continue
#                     if j<length-1 and nums[j]==nums[j+1]: 
#                         if nums[j]*2 ==targ: 
#                             tmp = nums[j]
#                             ans.append([0,cur,tmp,tmp])
#                         continue 
#                     next = nums[j]
#                     targ2 = targ-next
#                     if targ2 in mat:
#                         ans.append([0,cur,next,targ2])
#                     else:
#                         mat.add(next)
                        
#         if num_zero>=0:
            
            
#         return ans
            
            
        
    
        ans = []
        length = len(nums)
        for i in range(length-3):
            if i>0 and nums[i]==nums[i-1]: continue
            # n0 = nums[i]
            for j in range(i+1,length-2):
                if j>i+1 and nums[j]==nums[j-1]: continue
                n1 = nums[j]    
                targ = target - nums[i]-n1
                k = j+1 
                l = len(nums)-1
                
                while k<l:
                    if nums[k]+nums[l]<targ:
                        k+=1 
                    elif nums[k]+nums[l]>targ:
                        l-=1 
                    else:
                        ans.append([nums[i],n1,nums[k],nums[l]])
                    
                        low_ = nums[k]
                        high_ = nums[l]

                        while k<l and nums[k]==nums[k+1]:
                            k+=1
                        while k<l and nums[l]==nums[l-1]:
                            l-=1
                        k+=1
                        l-=1
                        
        
        return ans
        
        