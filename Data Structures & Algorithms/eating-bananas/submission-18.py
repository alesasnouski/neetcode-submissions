class Solution:
    def calcHours(self, piles: List[int], speed: int) -> int:
        hrs = 0
        import math
        for p in piles:
            hrs += math.ceil(p / speed)
        print(f"hrs:{hrs}::{speed}")
        return hrs    

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            m = l + (r - l) // 2
            mhours = self.calcHours(piles, m)
            if mhours <= h:
                res = min(res, m)
            if mhours <= h:
                r = m - 1
            else:
                l = m + 1
                
        return res
