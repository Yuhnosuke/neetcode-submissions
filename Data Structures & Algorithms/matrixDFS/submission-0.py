class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        def is_valid(row, column):
            return 0 <= row < rows and 0 <= column < columns


        def dfs(row, column):
            if not is_valid(row, column):
                return 0
            
            if (row, column) in visited:
                return 0
            
            if grid[row][column] == 1:
                return 0
            
            if row == rows - 1 and column == columns - 1:
                return 1

            visited.add((row, column))

            count = 0

            for dx, dy in directions:
                new_row, new_column = dy + row, dx + column
                count += dfs(new_row, new_column)


            visited.remove((row, column))

            return count


        return dfs(0, 0)