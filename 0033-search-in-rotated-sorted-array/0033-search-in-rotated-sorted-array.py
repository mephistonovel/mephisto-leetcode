class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pseudo-sorting된 리스트에서 target 찾기
        # bsearch 사용해야 하는듯
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        ###하나의 while loop 해결 - twopointers###
        
        init =0
        end = len(nums)-1
        
        while (init<=end):
            mid = init + (end-init)//2
            
            s = nums[init]
            m = nums[mid]
            e = nums[end]
            if m == target:
                return mid
            
            
            if (s<=m): #왼쪽이 작은경우
                # new_mid = init+(mid-init)//2
                if (target<=m and target>=s):
                    end = mid-1
                else:
                    init = mid+1
            else:
                if target>=m and target<=e: 
                    init = mid+1
                else:
                    end = mid-1
        
        return -1
                
                    
                
                
                    
                    

##################### faster 90.8, memory 15.36 #################
#         ans = -1
        
#         rot = nums[0]
#         ans = []
        
#         def findrot(nums,start,end,mid,rot):
#             if nums[start:end]:
#                 # print('rot',rot)
#                 # print('median',nums[mid])
#                 # print(rot>nums[mid])
                
#                 if rot>nums[mid] and nums[mid]<nums[mid-1]:
#                     ans.append(mid)
#                     return
#                 elif rot>nums[mid]:
                    
#                     if (end-start) % 2 ==1:
#                         new_start = mid -(end-1-mid)
#                     else:
#                         new_start = mid-(end-1-mid)-1
                        
#                     new_mid = new_start + (mid-new_start)//2
#                     findrot(nums,new_start,mid,new_mid,rot)
                    
#                 else: #rot<nums[mid]:
#                     new_mid = mid+1 + (end-(mid+1))//2
#                     findrot(nums,mid+1,end,new_mid,rot)
                    
            
#         def bsearch(nums,start,end,mid,target):
#             if nums[start:end]:
#                 if target>nums[mid]:
#                     new_mid = mid+1 + (end-(mid+1))//2
#                     bsearch(nums,mid+1,end,new_mid,target)
#                 elif target<nums[mid]:
#                     new_mid = start + (mid - start)//2
#                     bsearch(nums,start,mid,new_mid,target)
#                 else:
#                     final.append(mid)
#                     return
                    
                    
                    
#         # find rotate position by O(log n)
#         length = len(nums)
#         mid = len(nums)//2
#         findrot(nums,0,length,mid,rot)
#         rot_end = ans[0] if ans else None
        
#         if rot_end:

#             left = nums[:rot_end] #더 큰쪽
#             right = nums[rot_end:] #더 작은쪽
#             final = []
            
#             if target>right[-1]:
#                 start = 0
#                 end = len(left)
#                 mid = len(left)//2
#                 bsearch(left,start,end,mid,target)
#                 answer = final[0] if final else -1
#             else:
#                 start = 0
#                 end = len(right)
#                 mid = len(right)//2
#                 bsearch(right,start,end,mid,target)
#                 answer = rot_end + final[0] if final else -1 
#         else:
#             final = []
#             bsearch(nums,0,length,length//2,target)
#             answer = final[0] if final else -1
                
        
#         return answer