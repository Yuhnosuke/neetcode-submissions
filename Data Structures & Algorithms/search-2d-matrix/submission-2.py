class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        l, r = 0, rows * columns
        
        while l < r:
            m = (l + r) // 2
            row, column = m // columns, m % columns

            if matrix[row][column] > target:
                r = m
            elif matrix[row][column] < target:
                l = m + 1
            else:
                return True
        return False

