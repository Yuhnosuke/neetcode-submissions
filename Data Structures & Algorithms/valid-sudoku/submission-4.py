class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, columns = len(board), len(board[0])
        row_set, column_set, box_set = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == ".":
                    continue

                if board[r][c] in row_set[r] or board[r][c] in column_set[c] or board[r][c] in box_set[(r // 3, c // 3)]:
                    return False
                    
                row_set[r].add(board[r][c])
                column_set[c].add(board[r][c])
                box_set[(r // 3, c // 3)].add(board[r][c])
        
        return True

        