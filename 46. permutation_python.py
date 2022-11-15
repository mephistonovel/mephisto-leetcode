#https://devchoi.tistory.com/entry/%EB%A6%AC%ED%8A%B8%EC%BD%94%EB%93%9C-46-DFS%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%88%9C%EC%97%B4-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4 

class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        prev = []

        def dfs(arrays):
            if len(arrays) == 0:
                res.append(prev[:])
            
            for elem in arrays:
                prev.append(elem)
                dfs([e for e in arrays if e != elem])
                prev.pop()
                
        dfs(nums)
        return res
