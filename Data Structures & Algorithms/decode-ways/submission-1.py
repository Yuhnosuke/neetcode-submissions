class Solution:
    def numDecodings(self, s: str) -> int:
        def dp(i: int) -> i:
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = dp(i + 1) 
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6")):
                memo[i] += dp(i + 2)
            return memo[i]

        memo = {}
        return dp(0)
        