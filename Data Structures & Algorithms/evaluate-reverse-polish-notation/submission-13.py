class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            
            if token not in "+-*/":
                stack.append(int(token))
            else:       
                a, b = stack.pop(), stack.pop()
                tmp = 0
                if token == "+":
                    tmp = b + a
                if token == "-":
                    tmp = b - a
                if token == "*":
                    tmp = b * a
                if a != 0 and token == "/":
                    tmp = int(b / a)
                stack.append(tmp)

        return stack[-1]