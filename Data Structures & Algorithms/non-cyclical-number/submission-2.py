class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def is_cyclical(n):
            ns = sum((int(x) * int(x) for x in "%i" % n))
            if ns == 1:
                return True
            if ns in seen:
                return False
            seen.add(ns)
            return is_cyclical(ns)
        return is_cyclical(n)