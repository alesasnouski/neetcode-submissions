class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_bool = []
        for r in board:
            nums = []
            for x in r:
                if x.isnumeric():
                    nums.append(x)
            rows_bool.append(len(nums) == len(set(nums)))

        columns_bool = []
        for i in range(len(board)):
            nums = []
            for row in board:
                if row[i].isnumeric():
                    nums.append(row[i])
            columns_bool.append(len(nums) == len(set(nums)))

        group_bool = []
        items = [[0,1,2], [3,4,5], [6,7,8]]
        for il in items:
            for jl in items:
                nums = []
                for i in il:
                    for j in jl:
                        if board[i][j].isnumeric():
                            nums.append(board[i][j])
                group_bool.append(len(nums) == len(set(nums)))        

        print(group_bool)

        return all(columns_bool) and all(rows_bool) and all(group_bool)  