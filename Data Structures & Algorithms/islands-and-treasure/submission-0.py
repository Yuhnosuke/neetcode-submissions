from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        columns = len(grid[0])

        directions = [
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 0),
        ]

        def is_validated(row: int, column: int) -> bool:
            return 0 <= row < rows and 0 <= column < columns

        def bfs(queue, visited) -> int:
            while queue:
                row, column, steps = queue.popleft()

                if grid[row][column] == 0:
                    return steps
                visited.add((row, column))

                for dx, dy in directions:
                    new_row, new_column = row + dy, column + dx
                    if (new_row, new_column) not in visited and is_validated(new_row, new_column) and grid[new_row][new_column] != -1:
                        visited.add((new_row, new_column))
                        queue.append((new_row, new_column, steps + 1))

        
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2147483647:
                    grid[row][column] = bfs(deque([(row, column, 0)]), set())