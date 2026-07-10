class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {x:[] for x in range(len(points))}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                [xi, yi] = points[i]
                [xj, yj] = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        print(adj)
        res = 0
        visit = set()
        minH = [[0, 0]]
        while len(visit) < len(points):
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res
         