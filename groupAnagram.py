
def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    res_dict = dict()

    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in res_dict.keys():
            res_dict[sorted_word].append(word)
        else:
            res_dict[sorted_word] = [word]


    return res_dict.values()
  
if __

        
