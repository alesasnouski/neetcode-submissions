class Solution:
    from collections import deque

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        height = len(grid)
        width = len(grid[0])
        siblings = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        queue = deque([])
        fresh = 0
        steps = 0

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        while fresh > 0 and queue:
            qlen = len(queue)
            for k in range(qlen):
                (i0, j0) = queue.popleft()
                
                for [i1, j1] in siblings:
                    i = i0 + i1
                    j = j0 + j1

                    if i >= 0 and j >= 0 and i < height and j < width and grid[i][j] == 1:
                        grid[i][j] = 2
                        queue.append((i, j))
                        fresh -= 1

            steps = steps + 1
        
        return steps if fresh == 0 else -1