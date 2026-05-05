class Solution:
    def isValid(self, s: str) -> bool:
        open_close_bracket_map = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []

        for bracket in s:
            if bracket in open_close_bracket_map.keys():
                stack.append(bracket)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if open_close_bracket_map[popped] != bracket:
                        return False
        return True if len(stack) == 0 else False
            