class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l: int, r: int, res: int) -> None:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
            return res
            
        res = 0
        for center in range(len(s)):
            res = expand(center, center, res)
            res = expand(center, center + 1, res)
        return res

