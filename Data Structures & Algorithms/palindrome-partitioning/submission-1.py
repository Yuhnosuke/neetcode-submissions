class Solution:

    def is_palindrome(self, phrase: str, l: int, r: int) -> bool:
        while l < r:
            if phrase[l] != phrase[r]:
                return False
            l += 1
            r -= 1        
        return True

    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return []
        
        res = []
        curr = []

        def backtrack(start: int) -> None:
            if start == len(s):
                res.append(curr.copy())
                return
            
            for end in range(start, len(s)):
                if self.is_palindrome(s, start, end):
                    curr.append(s[start:end+1])
                    backtrack(end+1)
                    curr.pop()

        backtrack(0)
        return res
    