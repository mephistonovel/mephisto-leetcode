
def groupAnagrams(strs):
    """
    딕테이션이 핵심!! key를 찾을 때는 key in dict.keys()안하고 key in dict()해도 된다!! 
    :type strs: List[str]
    :rtype: List[List[str]]
    Runtime: 168 ms, faster than 42.51% of Python online submissions for Group Anagrams.
    Memory Usage: 17.3 MB, less than 82.02% of Python online submissions for Group Anagrams.
    https://leetcode.com/problems/group-anagrams/submissions/ 
    """
    res_dict = dict()

    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in res_dict:
            res_dict[sorted_word].append(word)
        else:
            res_dict[sorted_word] = [word]


    return res_dict.values()
  
if __name__ == '__main__':
    test =["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(test))
    
    """output: [["tan","nat"],["bat"],["eat","tea","ate"]]"""

        
