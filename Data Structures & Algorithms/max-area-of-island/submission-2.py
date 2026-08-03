class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r: int, c: int) -> int:
            # out of area
            if r < 0 or r >= rows or c < 0 or c >= columns:
                return 0
            # water
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            res = 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                res += dfs(dr + r, dc + c)
            return res

        rows = len(grid)
        columns = len(grid[0])
        res = 0
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res