class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nx = ["x" for x in range(0, len(nums) + 1)]
        for n in nums:
            nx[n] = n
        for i, x in enumerate(nx):
            if x == "x":
                return i
