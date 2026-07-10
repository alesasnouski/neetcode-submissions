class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1s = sorted(s1)
        s1len = len(s1)
        for i in range(len(s2)):
            subs = s2[i:s1len+i]
            if s1s == sorted(subs):
                return True
        return False        
        