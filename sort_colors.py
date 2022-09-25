"""
ex. 
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
https://medium.com/nerd-for-tech/75-sort-colors-15768309bf2f -> 1번째 방법 참고
"""

def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        len1 = 0
        len2 = 0
        len3 = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                len1+=1
            elif nums[i] == 1:
                len2+=1
            else:
                len3+=1
        
        j = 0
        
        while (len1 != 0):
            nums[j] = 0
            j+=1
            len1-=1 
            
        while (len2 != 0):
            nums[j] = 1
            j+=1
            len2-=1
            
        while (len3 !=0):
            nums[j] = 2
            j+=1
            len3 -= 1

if __name__ == '__main__':
    A = [2,0,2,1,1,0]
    sortColors(A)
    print(A)
