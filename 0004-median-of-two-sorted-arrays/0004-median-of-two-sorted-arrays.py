class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i1 = 0
        i2 = 0
        ans = []
        
        len1 = len(nums1)
        len2 = len(nums2)
        
        med_ = (len1+len2)//2
        rest = (len1+len2)%2
        if rest == 0:
            med_idx1, med_idx2 = med_-1,med_
        else:
            med_idx = med_
        
        i3 = 0
        while (i1<len1 and i2<len2):
            if nums1[i1] < nums2[i2]:
                ans.append(nums1[i1])
                i1+=1
            else:
                ans.append(nums2[i2])
                i2+=1   
            # i3+=1
        
        
        while (i1<len1):
            ans.append(nums1[i1])
            # i3+=1
            i1+=1

        while (i2<len2):
            ans.append(nums2[i2])
            # i3+=1
            i2+=1
            
        
        return ans[med_idx] if rest == 1 else (ans[med_idx1]+ans[med_idx2])/2
        