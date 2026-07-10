class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            an = abs(n)
            if nums[an - 1] < 0:
                return an
            else:
                nums[an - 1] = -1 * nums[an - 1]
                print(nums)