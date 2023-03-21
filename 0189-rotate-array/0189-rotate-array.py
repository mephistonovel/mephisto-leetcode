class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k=k%len(nums)
        # front = nums[-k:]
        # nums[:] = front+nums[:-k]
        
        #O(1)
        #https://leetcode.com/problems/rotate-array/discuss/3244055/Rotation-Array-
        
        def reverse(array,low,high):
            while low<high:
                tmp = array[low]
                array[low] = array[high]
                array[high]=tmp
                low+=1
                high-=1
        k = k%len(nums)
        n = len(nums)-1
        reverse(nums,0,n)
        reverse(nums,0,k-1)
        reverse(nums,k,n)