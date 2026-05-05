from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        queue = deque()
        queue.append((0, 0, 0))
        visited = set()
        visited.add((0, 0))

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        def is_validated(row, column):
            return 0 <= row < len(grid) and 0 <= column < len(grid[0])

        while queue:
            length_in_current_level = len(queue)

            for _ in range(length_in_current_level):
                row, column, level = queue.popleft()

                if row == len(grid) - 1 and column == len(grid[0]) - 1:
                    return level
                
                for dx, dy in directions:
                    new_row, new_column = dy + row, dx + column

                    if is_validated(new_row, new_column) and (new_row, new_column) not in visited and grid[new_row][new_column] == 0:
                        visited.add((new_row, new_column))
                        queue.append((new_row, new_column, level + 1))
            
        return -1


