class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        rows = len(grid)
        columns = len(grid[0])
        visited = set()

        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]

        def is_validated(row, column):
            return 0 <= row < rows and 0 <= column < columns and grid[row][column] == 1 and (row, column) not in visited

        def dfs(row, column):
            if not is_validated(row, column):
                return 0

            visited.add((row, column))
            answer = 1
            
            for dx, dy in directions:
                new_row, new_column = dx + row, dy + column
                answer += dfs(new_row, new_column)
            
            return answer

        for row in range(rows):
            for column in range(columns):
                if (row, column) not in visited and grid[row][column] == 1:                    
                    answer = max(answer, dfs(row, column))

        return answer