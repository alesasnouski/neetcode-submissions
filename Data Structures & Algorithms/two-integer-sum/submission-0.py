class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for (i, n0) in enumerate(nums):
            for (j, m1) in enumerate(nums):
                if i != j and len(res) == 0 and target == n0 + m1:
                    res = [i, j]
        return res