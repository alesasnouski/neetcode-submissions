class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        if target > nums[-1]:
            return "gt"
        elif target < nums[0]:
            return "lt"
        else:        
            while l <= r:
                # (l + r) // 2 can lead to overflow
                m = l + ((r - l) // 2)

                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return True 
            return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl = 0
        rr = len(matrix) - 1
        while rl <= rr:
            mr = rl + ((rr - rl) //2)
            if self.search(matrix[mr], target) == "lt":
                rr = mr - 1
            elif self.search(matrix[mr], target) == "gt":
                rl = mr + 1
            elif self.search(matrix[mr], target):
                return True
            else:
                return False    
        return False    