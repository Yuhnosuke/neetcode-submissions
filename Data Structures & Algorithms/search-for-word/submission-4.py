class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r: int, c: int, i: int, visited: set) -> bool:
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= columns:
                return False
            if (r, c) in visited:
                return False
            if board[r][c] != word[i]:
                return False
            
            visited.add((r, c))

            # r, c
            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),                
                (0, 1),                
            ]

            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1, visited):
                    return True
            visited.remove((r, c))
            return False

        rows = len(board)
        columns = len(board[0])

        visited = set()

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, visited):
                        return True
        return False
