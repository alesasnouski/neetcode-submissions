class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        d0 = defaultdict(int)
        d1 = defaultdict(int)
        for a in s:
            d0[a] += 1
        for b in t:
            d1[b] += 1
        return d0 == d1        