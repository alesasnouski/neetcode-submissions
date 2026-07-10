class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i, mcost):
            if i >= len(cost):
                return mcost
            return min(
                dfs((i + 1), mcost + cost[i]),
                dfs((i + 2), mcost + cost[i]),
            )
        return min(dfs(0, 0), dfs(1, 0))
