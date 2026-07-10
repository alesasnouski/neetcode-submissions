class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)
        return len(x) != len(nums)