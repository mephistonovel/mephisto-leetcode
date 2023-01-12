class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        if (len1 + len2) % 2 == 1:
            mid = (len1 + len2) // 2
            return self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, mid)
        else:
            mid1 = (len1 + len2 - 1) // 2
            mid2 = (len1 + len2) // 2
            median1 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, mid1)
            median2 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, mid2)
            return (median1 + median2)/2
    
    def get_kth(self, nums1, nums2, start1, end1, start2, end2, k):
        if start1 > end1:
            return nums2[k-start1]
        if start2 > end2:
            return nums1[k-start2]

        mid1 = start1 + (end1 - start1) // 2
        mid2 = start2 + (end2 - start2) // 2
        median1 = nums1[mid1]
        median2 = nums2[mid2]

        if mid1 + mid2 < k:
            if median1 < median2:
                return self.get_kth(nums1, nums2, mid1+1, end1, start2, end2, k)
            else:
                return self.get_kth(nums1, nums2, start1, end1, mid2+1, end2, k)
        else:
            if median1 < median2:
                return self.get_kth(nums1, nums2, start1, end1, start2, mid2-1, k)
            else:
                return self.get_kth(nums1, nums2, start1, mid1-1, start2, end2, k)
