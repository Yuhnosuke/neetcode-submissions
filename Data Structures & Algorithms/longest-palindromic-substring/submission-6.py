class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, res_len = "", 0

        def expand(l, r):
            nonlocal res_len, res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > res_len:
                    res = s[l:r+1]
                    res_len = curr_len
                l -= 1
                r += 1

        for center in range(len(s)):
            # odd length
            expand(center, center)
            # even length
            expand(center, center + 1)
        return res
