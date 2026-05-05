class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        rows = len(grid)
        columns = len(grid[0])
        visited = set()

        direction_deltas = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]

        def is_validate(row, column):
            return 0 <= row < rows and 0 <= column < columns and grid[row][column] == "1" and (row, column) not in visited

        def dfs(row, column):
            nonlocal answer
            for dx, dy in direction_deltas:
                new_row, new_column = dx + row, dy + column
                if is_validate(new_row, new_column):
                    visited.add((new_row, new_column))
                    dfs(new_row, new_column)
        
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1" and (row, column) not in visited:
                    answer += 1
                    visited.add((row, column))
                    dfs(row, column)

        return answer