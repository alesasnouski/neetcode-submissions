class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import copy
        result = {}
        for (i, n) in enumerate(nums):
            nums_reduced = copy.copy(nums)
            nums_reduced.pop(i)
            r = 1
            for x in nums_reduced:
                r *= x
            result[i] = r
        return list(result.values())