class Solution:
    def solve(self, board: List[List[str]]) -> None:
        keep_list = set()

        rows = len(board)
        columns = len(board[0])

        def is_validated(row: int, column: int) -> bool:
            return 0 <= row < rows and 0 <= column < columns

        directions = [
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 0),
        ]

        def dfs(row: int, column: int, visited: set) -> None:
            nonlocal keep_list

            if (row, column) in visited or not is_validated(row, column) or board[row][column] == "X":
                return
            
            visited.add((row, column))
            keep_list.add((row, column))

            for dx, dy in directions:
                new_row, new_column = dy + row, dx + column
                dfs(new_row, new_column, visited)

        for j in range(columns):
            if board[0][j] == "O":
                keep_list.add((0, j))
                dfs(0, j, set((0, j)))
            if board[rows - 1][j] == "O":
                keep_list.add((rows - 1, j))
                dfs(rows - 1, j, set((rows - 1, j,)))
        
        for i in range(rows):
            if board[i][0] == "O":
                keep_list.add((i, 0))
                dfs(i, 0, set((i, 0)))
            if board[i][columns - 1] == "O":
                keep_list.add((i, columns - 1))
                dfs(i, columns - 1, set((i, columns - 1)))
        
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == "O" and (i, j) not in keep_list:
                    board[i][j] = "X"

