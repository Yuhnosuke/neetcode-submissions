class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        reachables = []
        ROWS = len(heights)
        COLUMNS = len(heights[0])
        
        def is_reachable_helper(r: int, c: int, visited: set, is_pacific: bool, pr: int, pc: int) -> bool:
            if not (0 <= r < ROWS and 0 <= c < COLUMNS):
                return False
            
            if (r, c) in visited:
                return False
            
            if heights[r][c] > heights[pr][pc]:
                return False

            if is_pacific:
                if r == 0 or c == 0:
                    return True
            else:
                if r == ROWS - 1 or c == COLUMNS - 1:
                    return True
            
            visited.add((r, c))

            for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = dy + r, dx + c
                
                if is_reachable_helper(nr, nc, visited, is_pacific, r, c):
                    return True

            return False


        def is_reachable(r: int, c: int) -> bool:
            return is_reachable_helper(r, c, set(), True, r, c) and is_reachable_helper(r, c, set(), False, r, c)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if is_reachable(r, c):
                    reachables.append([r, c])

        return reachables

