class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        check =0
        mid_point = len(nums)//2
        init = 0
        end = len(nums)
        def bsearch(num_list,targ,ans,mid_point,init,end):
            if num_list[init:end]:
                if targ>num_list[mid_point]:
                    tmp_mid = mid_point+1 + (end-(mid_point+1))//2
                    bsearch(num_list,targ,ans,tmp_mid,mid_point+1,end)
                elif targ<num_list[mid_point]:
                    mid_plus = (mid_point-init)//2
                    tmp_mid = init+ mid_plus
                    bsearch(num_list,targ,ans,tmp_mid,init,mid_point)
                else:
                    ans.append(mid_point)
                    tmp_mid1 = init+(mid_point-init)//2
                    tmp_mid2 = mid_point+1 + (end - (mid_point+1))//2
                    bsearch(num_list,targ,ans,tmp_mid1,init,mid_point)
                    bsearch(num_list,targ,ans,tmp_mid2,mid_point+1,end)
                    return None
                        
        bsearch(nums,target,ans,mid_point,init,end)
        
        if ans:
            ans.sort()
            return [ans[0],ans[-1]]
        else:
            return [-1,-1]
        
