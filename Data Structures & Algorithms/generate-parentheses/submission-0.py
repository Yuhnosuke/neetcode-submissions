class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open_p, close_p):
            if open_p == close_p == n:
                res.append("".join(stack))
                return
            
            if open_p < n:
                stack.append("(")
                backtrack(open_p + 1, close_p)
                stack.pop()
            if close_p < open_p:
                stack.append(")")
                backtrack(open_p, close_p + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
        