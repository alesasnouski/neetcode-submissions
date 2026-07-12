class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(0, len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0]) // 2):
                l = len(matrix[0]) - 1 - j
                matrix[i][j], matrix[i][l] = matrix[i][l], matrix[i][j]
        print(matrix)


#    0  1  2  3  4
#    4, 5, 6, 7, 8