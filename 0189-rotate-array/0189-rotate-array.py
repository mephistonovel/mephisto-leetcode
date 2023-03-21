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
        # if len(nums)<=1 or k==len(nums):
        #     pass
        # elif len(nums)-k<=1:
        #     tmp0 = nums[0]
        #     nums[0]=nums[1]
        #     for i in range(1,len(nums)-1):
        #         nums[i] = nums[i+1]
        #     nums[-1] = tmp0
        # else:
        #     for i in range(k,0,-1):
        #         print(k,i)
        #         tmp = nums[-i] # nums[-3]
        #         robbed = nums[k-i] # nums[3-3]=nums[0]
        #         swap = nums[k-i+k] # nums[3+3-3] = nums[3]
        #         nums[k-i] = tmp
        #         nums[-i]=swap
        #         nums[k+k-i]=robbed
            