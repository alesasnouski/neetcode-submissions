class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for x in nums:
            to_add = []
            for r in result:
                to_add.append(r + [x])
            result = result + to_add
        return result
