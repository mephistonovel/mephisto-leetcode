class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       
        index1=-1
        index2=0
        check = True
        length = len(nums)
        for i in range(length):
            num2_can = target - nums[i]
            index1+=1
            for j in range(i,length):
                if (nums[j] == num2_can) and (i != j):
                    # print(index22,num2)
                    index2=j
                    check = False
                    break
            if (check == False):
                break

        return [index1,index2]




            # if (num2_can in nums):
            #     index1=nums.index(num1)
            #     index2=nums.index(num2_can)
            #     break


                
                

