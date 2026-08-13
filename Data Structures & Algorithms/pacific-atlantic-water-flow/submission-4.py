class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_reachables, atlantic_reachables = set(), set()
        
        ROWS = len(heights)
        COLUMNS = len(heights[0])

        def add_reachable(r, c, reachables, pr, pc):
            if not (0 <= r < ROWS and 0 <= c < COLUMNS):
                return 

            if (r, c) in reachables:
                return 

            if heights[r][c] < heights[pr][pc]:
                return 
            
            reachables.add((r, c))

            for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                add_reachable(dy + r, dx + c, reachables, r, c)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if r == 0 or c == 0:
                    add_reachable(r, c, pacific_reachables, r, c)
                if r == ROWS - 1 or c == COLUMNS - 1:
                    add_reachable(r, c, atlantic_reachables, r, c)

        ans = []
        for r, c in (pacific_reachables & atlantic_reachables):
            ans.append([r, c])
        return ans