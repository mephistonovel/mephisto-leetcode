class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) >len(s2):
            return False

        step = len(s1)
        s1count = Counter(s1)

        i=0
        while i<len(s2)-step+1:    
            s22=Counter(s2[i:i+step])
            if s1count==s22:
                return True
            i+=1 
        return False

        