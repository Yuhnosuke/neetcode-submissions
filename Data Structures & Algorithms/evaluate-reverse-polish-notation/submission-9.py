class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(0, len(tokens)):
            if tokens[i] in "+-*/":
                operand_a = stack.pop()
                operand_b = stack.pop()
                calc_result = 0
                if tokens[i] == "+":
                    calc_result = operand_b + operand_a
                if tokens[i] == "-":
                    calc_result = operand_b - operand_a
                if tokens[i] == "*":
                    calc_result = operand_b * operand_a
                if tokens[i] == "/":
                    calc_result = int(operand_b / operand_a)
                stack.append(calc_result)
            else:
                stack.append(int(tokens[i]))
                    
        
        return stack[-1]
