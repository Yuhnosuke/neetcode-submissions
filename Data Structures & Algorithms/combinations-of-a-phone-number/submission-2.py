class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digit_to_chars = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []
        curr = []

        def backtrack(di):
            if di == len(digits):
                res.append("".join(curr))
                return
            
            for ch in digit_to_chars[digits[di]]:
                curr.append(ch)
                backtrack(di + 1)
                curr.pop()
        
        backtrack(0)
        return res

