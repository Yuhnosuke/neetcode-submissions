class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1],
        ]
        
        def dfs(r: int, c: int) -> None:

            for dy, dx in directions:
                if dy + r < 0 or dy + r >= rows or dx + c < 0 or dx + c >= columns:
                    continue
                if (dy + r, dx + c) in visited:
                    continue
                
                if grid[dy + r][dx + c] == "0":
                    continue
            
                visited.add((dy + r, dx + c))
                dfs(dy + r, dx + c)

        res = 0

        rows = len(grid)
        columns = len(grid[0])

        visited = set()

        for r in range(rows):
            for c in range(columns):
                if (r, c) not in visited and grid[r][c] == "1":
                    visited.add((r, c))
                    dfs(r, c)
                    res += 1

        return res

