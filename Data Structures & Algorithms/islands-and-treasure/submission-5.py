class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        columns = len(grid[0])
        LAND = 2147483647
        
        to_right = [0, 1]
        to_left = [0, -1]
        to_bottom = [1, 0]
        to_top = [-1, 0]
        directions = [to_right, to_left, to_bottom, to_top]

        def is_land(r, c):
            return grid[r][c] == LAND

        def is_treasure(r, c):
            return grid[r][c] == 0
       
        def is_in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < columns
       
        def is_water(r, c):
            return grid[r][c] == -1
        
        q = deque([])
        visited = set()

        for r in range(rows):
            for c in range(columns):
                if is_treasure(r, c):
                    q.append((r, c, 0)) # (r, c, distance)
                    visited.add((r, c))

        while q:
            r, c, distance = q.popleft()
            grid[r][c] = distance
            
            for dy, dx in directions:
                nr, nc = dy + r, dx + c

                if not is_in_bounds(nr, nc):
                    continue
                
                if is_water(nr, nc):
                    continue
                
                if (nr, nc) in visited:
                    continue

                visited.add((nr, nc))                        
                q.append((nr, nc, distance + 1))

        


