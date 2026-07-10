class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return

        results = []
        height = len(grid)
        width = len(grid[0])
        dimensions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        def dfs(i, j, size):
            print(f"{i}:{j}")
            if i < 0 or j < 0 or i >= height or j >= width or grid[i][j] == 0:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 0
                final_size = size + 1
                for d in dimensions:
                    final_size += dfs(i+d[0], j+d[1], 0)
                return final_size    


        for i in range(height):
            for j in range(width):
                results.append(dfs(i, j, 0))
        
        return max(results)
        