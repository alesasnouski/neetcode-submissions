class Solution:
    def __init__(self):
        self.islands = 0 

    def numIslands(self, grid: List[List[str]]) -> int:
        width = len(grid[0])
        height = len(grid)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= height or j >= width or grid[i][j] == "0":
                return
            grid[i][j] = "0"

            for (k, l) in directions:
                dfs(i + k, j + l)
       
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    self.islands += 1
                    dfs(i, j)

        return self.islands
                