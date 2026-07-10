class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i > n:
                return 0
            elif i == n:
                return 1
            else:
                return dfs(i + 1) + dfs(i + 2)
        return dfs(0)