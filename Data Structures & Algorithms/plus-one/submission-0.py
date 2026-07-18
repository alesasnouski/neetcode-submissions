class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(x) for x in digits]
        inc = int("".join(digits)) + 1
        return [int(x) for x in "%s" % inc]