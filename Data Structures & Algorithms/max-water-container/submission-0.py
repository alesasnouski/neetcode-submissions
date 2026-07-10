class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) <= 1:
            return 0
        j = len(heights) - 1
        i = 0
        res = 0
        while True:
            if i == j:
                break
            volume = (j - i) * min(heights[i], heights[j])
            if volume > res:
                res = volume
            if heights[i] >= heights[j]:
                j = j - 1
            else:
                i = i + 1

        return res                