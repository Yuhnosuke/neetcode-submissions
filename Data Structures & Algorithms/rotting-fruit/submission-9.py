class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0

        ROWS = len(grid)
        COLUMNS = len(grid[0])
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        VISITED = 3        
        q = deque()

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == ROTTEN:
                    q.append((r, c, 0)) # (r, c, t)
                    grid[r][c] = VISITED

        while q:
            r, c, t = q.popleft()
            minutes = t

            for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = dy + r, dx + c                
                
                if not (0 <= nr < ROWS and 0 <= nc < COLUMNS):
                    continue
                    
                if grid[nr][nc] == VISITED:
                    continue
                
                if grid[nr][nc] == EMPTY:
                    continue
                
                q.append((nr, nc, t + 1))
                grid[nr][nc] = VISITED

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == FRESH:
                    return -1
        return minutes
