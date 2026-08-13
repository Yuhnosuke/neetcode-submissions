class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        reachables = []
        ROWS = len(heights)
        COLUMNS = len(heights[0])

        def is_pacific_reachable(r: int, c: int, visited: set) -> bool:
            if r == 0 or c == 0:
                return True

            visited.add((r, c))

            for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = dy + r, dx + c

                if not (0 <= nr < ROWS and 0 <= nc < COLUMNS):
                    continue

                if (nr, nc) in visited:
                    continue
                
                if heights[nr][nc] > heights[r][c]:
                    continue
                
                if is_pacific_reachable(nr, nc, visited):
                    return True

            return False

        def is_atrantic_reachable(r: int, c: int, visited: set) -> bool:
            if r == ROWS - 1 or c == COLUMNS - 1:
                return True
            
            visited.add((r, c))

            for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = dy + r, dx + c
                if not (0 <= nr < ROWS and 0 <= nc < COLUMNS):
                    continue

                if (nr, nc) in visited:
                    continue
                
                if heights[nr][nc] > heights[r][c]:
                    continue
                
                if is_atrantic_reachable(nr, nc, visited):
                    return True

            return False

        def is_reachable(r: int, c: int) -> bool:
            return is_pacific_reachable(r, c, set()) and is_atrantic_reachable(r, c, set())

        for r in range(ROWS):
            for c in range(COLUMNS):
                if is_reachable(r, c):
                    reachables.append([r, c])

        return reachables

