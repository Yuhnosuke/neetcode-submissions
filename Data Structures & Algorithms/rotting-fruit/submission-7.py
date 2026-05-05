from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        num_of_fresh = 0
        visited = set()
        queue = deque([])
        
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    num_of_fresh += 1
                if grid[row][column] == 2:
                    queue.append((row, column, 0))
                    visited.add((row, column))
                    
        directions = [
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 0),
        ]
        def is_validated(row, column):
            return 0 <= row < rows and 0 <= column < columns


        answer = 0
        while queue:
            nodes_in_current_level = len(queue)
            for _ in range(nodes_in_current_level):
                row, column, steps = queue.popleft()

                for dx, dy in directions:
                    new_row, new_column = row + dy, column + dx
                    if is_validated(new_row, new_column) and (new_row, new_column) not in visited and grid[new_row][new_column] == 1:
                        visited.add((new_row, new_column))
                        queue.append((new_row, new_column, steps + 1))
                        answer = steps + 1
                        num_of_fresh -= 1

        if num_of_fresh > 0:
            return -1

        return answer