class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        for (n, i) in enumerate(numbers):
            m[i] = n

        for num in numbers:
            if target - num in m:
                return [m[num] + 1, m[target - num] + 1]  