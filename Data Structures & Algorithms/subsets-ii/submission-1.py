class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        nums = sorted(nums)
        if len(nums) == 0:
            return perms
        else:
            for i, n in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                rst = nums[i+1:]
                for p in self.subsetsWithDup(rst):
                    perms.append([n] + p)
        return perms