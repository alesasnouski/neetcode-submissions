class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board

        rows = len(board)
        cols = len(board[0])

        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs(i, j):
            for (i0, j0) in directions:
                i1 = i + i0
                j1 = j + j0
                if i1 >= 0 and j1 >= 0 and i1 < rows and j1 < cols and board[i1][j1] == 'O':
                    board[i1][j1] = 'T'
                    dfs(i1, j1)

        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows - 1 or j == cols - 1):
                    if board[i][j] == 'O':
                        board[i][j] = 'T'
                        dfs(i, j)
                        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
            
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
