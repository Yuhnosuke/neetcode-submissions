class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        l, r = 0, rows * columns
        
        while l < r:
            m = (l + r) // 2
            row = m // columns
            column = m % columns
            if matrix[row][column] == target:
                return True
            if matrix[row][column] >= target:
                r = m
            else:
                l = m + 1
        return False
            