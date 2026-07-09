class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(curr: List[str], remaining_start: int, curr_start, curr_close) -> None:
            if len(curr) == 2 * n:
                res.append("".join(curr))
                return

            if remaining_start > 0:
                curr.append("(")
                backtrack(curr, remaining_start - 1, curr_start + 1, curr_close)
                curr.pop()

            if curr_start > curr_close:
                curr.append(")")
                backtrack(curr, remaining_start, curr_start, curr_close + 1)
                curr.pop()
                
        res = []
        curr = []
  
        backtrack(curr, n, 0, 0)
        return res

