class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                prev1, prev2 = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(prev2 + prev1)
                elif token == "-":
                    stack.append(prev2 - prev1)
                elif token == "*":
                    stack.append(prev2 * prev1)
                else:
                   stack.append(int(prev2 / prev1)) 
            else:
                stack.append(int(token))

        return stack[-1]        
        