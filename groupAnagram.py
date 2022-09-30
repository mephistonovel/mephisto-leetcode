
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    Runtime: 3414 ms, faster than 5.00% of Python online submissions for Group Anagrams.
    Memory Usage: 17.3 MB, less than 89.37% of Python online submissions for Group Anagrams.
    https://leetcode.com/problems/group-anagrams/submissions/ 
    """
    res_dict = dict()

    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in res_dict.keys():
            res_dict[sorted_word].append(word)
        else:
            res_dict[sorted_word] = [word]


    return res_dict.values()
  
if __name__ == '__main__':
    test =["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(test))
    
    """output: [["tan","nat"],["bat"],["eat","tea","ate"]]"""

        
