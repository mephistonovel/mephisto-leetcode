class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """https://leetcode.com/problems/next-permutation/discuss/1909728/Simple-9-line-Python-Solution-with-Detailed-Explanation-(Easy-Understand-for-Beginners!) """
        
        # 1,4,2,3 
        
        #corner case
        if nums == sorted(nums,reverse=True):
            nums.sort()
        
        else:
            for i in range(len(nums)-1,0,-1):
                if nums[i-1]<nums[i]:
                    print(i) # 3
                    nums[i:] = sorted(nums[i:])
                
                swap_pos = -1
                for j in range(i,len(nums)):
                    if nums[i-1]<nums[j]:
                        print('swap_pos',j) # 3 과 2 바꾸기 
                        swap_pos = j
                        nums[i-1], nums[swap_pos] = nums[swap_pos],nums[i-1]
                        return nums
            
        