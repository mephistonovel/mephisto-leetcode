#https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        used = [0 for _ in range(len(nums))]
        

        def generate(prev,used):
            if len(prev)==len(nums):
                res.append(prev[:])
            else:
                for i in range(len(nums)):
                    if (not used[i]) and (i==0 or nums[i]!=nums[i-1] or used[i-1]):
                        prev.append(nums[i])
                        used[i] = 1
                        generate(prev,used)
                        used[i] = 0
                        prev.pop()
        
        generate([],used)

        return res
