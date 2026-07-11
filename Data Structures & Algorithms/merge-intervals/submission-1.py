class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals)
        for i in range(1, len(intervals)):
            if intervals[i][0] > intervals[i-1][1]:
                result.append(intervals[i-1])
            else:
                intervals[i] = [
                    min(intervals[i-1][0], intervals[i][0]),
                    max(intervals[i-1][1], intervals[i][1]) 
                ]
        result.append(intervals[-1])
        return result