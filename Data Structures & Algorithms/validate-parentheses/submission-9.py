class Solution:
    def isValid(self, s: str) -> bool:    
        open_to_close = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        stack = []
        for ch in s:
            if ch in open_to_close.keys():
                stack.append(ch)
            if ch in open_to_close.values():
                if not stack:
                    return False
                if open_to_close[stack[-1]] != ch:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
            