class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        if len(nums) <= 1:
            return [nums[:]]
        for i, n in enumerate(nums):
            rest = nums[:i] + nums[i+1:]
            for p in self.permute(rest):
                perms.append(p + [n])
        return perms

