class Solution:
    def numDecodings(self, s: str) -> int:
        def dp(i):
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            if i in memo:
                return memo[i]
            
            answer = dp(i + 1)

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                answer += dp(i + 2)
            
            memo[i] = answer

            return answer


        memo = {}
        return dp(0)