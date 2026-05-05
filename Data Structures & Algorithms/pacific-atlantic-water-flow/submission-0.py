class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])

        reachables_to_pacific = set()
        reachables_to_atlantic = set()

        def is_validated(row: int, column: int) -> bool:
            return 0 <= row < rows and 0 <= column < columns
        
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        def dfs(row: int, column: int, reachables: set(), previous_height: int) -> None:
            if (row, column) in reachables or not is_validated(row, column) or heights[row][column] < previous_height:
                return
            
            reachables.add((row, column))
            
            for dx, dy in directions:
                new_row, new_column = dy + row, dx + column
                dfs(new_row, new_column, reachables, heights[row][column])

        for column in range(columns):
            dfs(0, column, reachables_to_pacific, heights[0][column])
            dfs(rows - 1, column, reachables_to_atlantic, heights[rows - 1][column])
        
        for row in range(rows):
            dfs(row, 0, reachables_to_pacific, heights[row][0])
            dfs(row, columns - 1, reachables_to_atlantic, heights[row][columns - 1])
        
        answer = []
        for row in range(rows):
            for column in range(columns):
                if (row, column) in reachables_to_pacific and (row, column) in reachables_to_atlantic:
                    answer.append([row, column])
        
        return answer