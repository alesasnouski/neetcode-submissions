from functools import reduce

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            return reduce(lambda x, y: x * y, (x for i in range(0, n)))
        else:
            return reduce(lambda x, y: x * y, (1/x for i in range(0, -1 * n)))