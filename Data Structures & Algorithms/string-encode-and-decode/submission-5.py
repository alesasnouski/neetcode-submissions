class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            slen = len(s)
            result = result + f"{slen}" + "#" + s + "#"

        return result    

    def decode(self, s: str) -> List[str]:
        result = []
        l, r = 0, 1
        print(s)
        while r < len(s):
            while s[l:r].isdigit():
                r = r + 1
            r = r - 1    
            print(l)
            print(r)
            lngth = int(s[l:r])
            strng = s[r+1: r + lngth + 1]
            result.append(strng)
            l = r + 2 + lngth
            r = r + 3 + lngth
        return result