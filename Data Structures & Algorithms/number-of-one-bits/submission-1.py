class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):
            count += n & 1      # смотрим младший бит
            n >>= 1             # сдвигаем вправо
        return count