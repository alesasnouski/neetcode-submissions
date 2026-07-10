from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for i,j,t in times:
            adj[i].append((j, t))
        
        dist = {i: float("inf") for i in range(1, n + 1)}

        def dfs(node, time):
            if time > dist[node]:
                return
            dist[node] = time

            for n, t in adj[node]:
                dfs(n, time + t)

        dfs(k, 0)
        res = max(dist.values())
        return res if res < float("inf") else -1