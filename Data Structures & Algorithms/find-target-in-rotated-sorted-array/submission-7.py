class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                res = m
                break
            if nums[l] == target:
                res= l 
                break
            if nums[r] == target:
                res = r
                break
            if nums[m] >= nums[l]:
                l = l + 1
            else:
                r = m - 1
        return res            
