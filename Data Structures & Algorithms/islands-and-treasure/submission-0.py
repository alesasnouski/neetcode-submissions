class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        height = len(grid)
        width = len(grid[0])
        inf = 2**31 - 1
        siblings = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        def dfs(i, j, step):
            for [i0, j0] in siblings:
                i1 = i + i0
                j1 = j + j0
                if i1 >= 0 and j1 >= 0 and i1 < height and j1 < width: 
                    if grid[i1][j1] == inf:
                        grid[i1][j1] = step
                        dfs(i1, j1, step + 1)
                    elif grid[i1][j1] > 0 and grid[i1][j1] > step:
                        grid[i1][j1] = step
                        dfs(i1, j1, step + 1)
                    
                    
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    dfs(i, j, 1)