class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervalz = sorted(intervals)
        result = 0
        if len(intervalz) <= 1:
            return result
        for i in range(1, len(intervalz)):
            if intervalz[i][0] < intervalz[i-1][1]:
                result += 1
                if intervalz[i-1][1] < intervalz[i][1]:
                    intervalz[i] = intervalz[i-1]
        return result