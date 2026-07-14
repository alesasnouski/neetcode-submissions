class Solution:
    def cycle(self, matrix, top, bottom, left, right, result):
        if top > bottom or left > right:
            return

        # верх: слева направо
        for j in range(left, right + 1):
            result.append(matrix[top][j])

        # правый столбец: сверху вниз
        for i in range(top + 1, bottom + 1):
            result.append(matrix[i][right])

        # низ: справа налево (только если строка не та же самая)
        if top < bottom:
            for j in range(right - 1, left - 1, -1):
                result.append(matrix[bottom][j])

        # левый столбец: снизу вверх (только если столбец не тот же самый)
        if left < right:
            for i in range(bottom - 1, top, -1):
                result.append(matrix[i][left])

        self.cycle(matrix, top + 1, bottom - 1, left + 1, right - 1, result)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        result = []
        self.cycle(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1, result)
        return result