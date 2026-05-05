class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        parentheses = []

        for bracket in s:
            if bracket in open_to_close.keys():
                parentheses.append(bracket)
            else:
                if not parentheses or open_to_close[parentheses[-1]] != bracket:
                    return False
                parentheses.pop()
        if parentheses:
            return False
        return True