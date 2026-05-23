class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        l, r = 0, rows * columns

        while l < r:
            m = (l + r) // 2

            row = m // columns
            col = m % columns

            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] > target:
                r = m
            else:
                l = m + 1
        return False