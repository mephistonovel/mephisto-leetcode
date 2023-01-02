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
        for num1 in nums:
            num2_can = target - num1
            index1+=1
            for index22,num2 in enumerate(nums):
                if (num2 == num2_can) and (index1 != index22):
                    # print(index22,num2)
                    index2=index22
                    check = False
                    break
            if (check == False):
                break

        return [index1,index2]




            # if (num2_can in nums):
            #     index1=nums.index(num1)
            #     index2=nums.index(num2_can)
            #     break


                
                

