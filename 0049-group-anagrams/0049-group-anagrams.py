class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        
        for elem in strs:
            key = ''.join(sorted(list(elem)))
            # print(key)
            if key not in ans:
                ans[key] = [elem]
            else:
                ans[key].append(elem)
        
        return ans.values()