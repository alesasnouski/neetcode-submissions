class Solution:
    def distance(self, point):
            [x1, y1] = point
            import math
            return math.sqrt(pow(x1, 2) + pow(y1, 2))


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        l = []

        for point in points:
            heapq.heappush(l, (self.distance(point), point))

        res = []
        while k > 0:
            res.append(heapq.heappop(l))
            k -=1
        return [x[1] for x in res]     